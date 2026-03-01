#!/usr/bin/env python3
"""
Generate editable draw.io (.drawio) architecture diagrams from JSON descriptions.

Produces mxGraph XML files that open in draw.io desktop or https://app.diagrams.net.
Uses the same JSON input schema as generate_architecture_diagram.py (Graphviz)
with optional draw.io-specific extensions (layout direction, edge routing,
multi-page support, style overrides).

Rendering notes:
  - Output is uncompressed XML (draw.io handles both compressed and uncompressed).
  - Zones render as swimlane containers — collapsible/expandable in the editor.
  - Component shapes and colours match the existing Graphviz mappings exactly.
  - Edge routing mode is stored in edge styles; draw.io calculates actual paths.

Usage:
    python generate_drawio_diagram.py \\
        -d description.json -o diagram.drawio [--layout LR] [--edge-routing orthogonal]

Example description.json (same as Graphviz script):
{
  "title": "System Architecture",
  "zones": [
    {
      "name": "On Premise Architecture",
      "components": ["SQL Database", "Email Inboxes", "SAP Endpoint"]
    },
    {
      "name": "Azure Virtual Network",
      "color": "#0078D4",
      "components": ["VPN Gateway", "Quotation Pipeline", "LLM Endpoint",
                      "Webapp", "Draft DB"]
    }
  ],
  "components": [
    {"name": "SQL Database",        "type": "database"},
    {"name": "Email Inboxes",       "type": "client"},
    {"name": "SAP Endpoint",        "type": "external"},
    {"name": "VPN Gateway",         "type": "gateway"},
    {"name": "Quotation Pipeline",  "type": "service"},
    {"name": "LLM Endpoint",        "type": "ai"},
    {"name": "Webapp",              "type": "client"},
    {"name": "Draft DB",            "type": "database"}
  ],
  "flows": [
    {"from": "Email Inboxes",       "to": "VPN Gateway",         "label": "Read emails"},
    {"from": "SQL Database",        "to": "VPN Gateway",         "label": "Load relevant data"},
    {"from": "VPN Gateway",         "to": "Quotation Pipeline",  "label": ""},
    {"from": "Quotation Pipeline",  "to": "LLM Endpoint",        "label": "LLM information extraction"},
    {"from": "Quotation Pipeline",  "to": "Draft DB",            "label": "Store quotations"},
    {"from": "Webapp",              "to": "Draft DB",            "label": "Fetch quotations"},
    {"from": "Webapp",              "to": "SAP Endpoint",        "label": "Save confirmed quotations"}
  ]
}

Extended fields (optional, draw.io-specific):
  "layout": {"direction": "LR"|"TB", "spacing": {"horizontal": 200, "vertical": 150},
              "edge_routing": "orthogonal"|"curved"|"straight"}
  "style_overrides": {"fillColor": "#custom"} on any component
  "pages": [{"name": "Page Name", "zones": [...], "components": [...], "flows": [...]}]
"""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Component type → draw.io shape + colour mappings
# (identical colours to Graphviz script for backward compatibility)
# ---------------------------------------------------------------------------

SHAPE_MAP: Dict[str, str] = {
    "client":   "rounded=1;",
    "service":  "rounded=1;",
    "database": "shape=cylinder3;size=15;whiteSpace=wrap;",
    "external": "shape=component;align=center;",
    "gateway":  "shape=mxgraph.basic.shaded_box;",
    "ai":       "shape=hexagon;perimeter=hexagonPerimeter2;size=0.15;",
    "queue":    "shape=parallelogram;perimeter=parallelogramPerimeter;",
    "cache":    "shape=mxgraph.basic.octagon;",
    "message":  "shape=message;",
}

FILL_MAP: Dict[str, str] = {
    "client":   "#E1F5FF",
    "service":  "#F3E5F5",
    "database": "#E8F5E9",
    "external": "#FFF3E0",
    "gateway":  "#F3E5F5",
    "ai":       "#E3F2FD",
    "queue":    "#F1F8E9",
    "cache":    "#FCE4EC",
    "message":  "#FCE4EC",
}

BORDER_MAP: Dict[str, str] = {
    "client":   "#01579B",
    "service":  "#4A148C",
    "database": "#1B5E20",
    "external": "#E65100",
    "gateway":  "#4A148C",
    "ai":       "#0D47A1",
    "queue":    "#33691E",
    "cache":    "#880E4F",
    "message":  "#880E4F",
}

DEFAULT_ZONE_COLOR = "#999999"
DEFAULT_ZONE_BG = "#FAFAFA"

# Edge routing mode → mxGraph edge style string
EDGE_STYLE_MAP: Dict[str, str] = {
    "orthogonal": "edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;jettySize=auto;",
    "curved":     "edgeStyle=orthogonalEdgeStyle;curved=1;orthogonalLoop=1;jettySize=auto;",
    "straight":   "edgeStyle=none;",
}

# Layout constants
COMP_WIDTH = 160
COMP_HEIGHT = 60
ZONE_PADDING = 30
ZONE_HEADER_HEIGHT = 30
ZONE_GAP = 60
COMP_GAP_H = 40
COMP_GAP_V = 30


# ---------------------------------------------------------------------------
# Colour utilities
# ---------------------------------------------------------------------------

def _lighten(hex_color: str) -> str:
    """Return a very light tint (85% white blend) for zone backgrounds."""
    h = hex_color.lstrip("#")
    try:
        r, g, b = int(h[:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        r = int(r * 0.15 + 255 * 0.85)
        g = int(g * 0.15 + 255 * 0.85)
        b = int(b * 0.15 + 255 * 0.85)
        return f"#{r:02X}{g:02X}{b:02X}"
    except (ValueError, IndexError):
        return DEFAULT_ZONE_BG


# ---------------------------------------------------------------------------
# ID management
# ---------------------------------------------------------------------------

class IdAllocator:
    """Sequential integer IDs for mxCell elements.

    mxGraph requires unique integer IDs. Cell 0 is the root model,
    cell 1 is the default parent layer.
    """

    def __init__(self, start: int = 2):
        self._next = start

    def next(self) -> str:
        val = self._next
        self._next += 1
        return str(val)


# ---------------------------------------------------------------------------
# Layout engine
# ---------------------------------------------------------------------------

def _compute_zone_layout(
    zones: List[Dict[str, Any]],
    components: Dict[str, Dict[str, Any]],
    direction: str,
    h_spacing: int,
    v_spacing: int,
) -> Dict[str, Any]:
    """Compute positions for zones and their components.

    Returns a dict with:
      zone_rects: list of {name, x, y, w, h, color, bgcolor, comp_names}
      comp_positions: {comp_name: (x, y)}  — absolute positions
      ungrouped_positions: {comp_name: (x, y)} — components not in any zone
    """
    zone_rects: List[Dict[str, Any]] = []
    comp_positions: Dict[str, tuple] = {}
    placed: set = set()

    # Determine how many columns of components fit inside a zone
    # For LR layout: zones arranged left→right, components stacked vertically
    # For TB layout: zones arranged top→bottom, components stacked horizontally
    is_lr = direction.upper() == "LR"

    cursor_x = ZONE_PADDING
    cursor_y = ZONE_PADDING

    for zone in zones:
        zone_name = zone.get("name", "Zone")
        zone_comps = zone.get("components", [])
        zone_color = zone.get("color", DEFAULT_ZONE_COLOR)
        zone_bg = zone.get("bgcolor",
                           DEFAULT_ZONE_BG if zone_color == DEFAULT_ZONE_COLOR
                           else _lighten(zone_color))
        n = len(zone_comps)
        if n == 0:
            continue

        if is_lr:
            # Stack components vertically within the zone
            inner_w = COMP_WIDTH + 2 * ZONE_PADDING
            inner_h = (n * COMP_HEIGHT + (n - 1) * COMP_GAP_V
                       + ZONE_HEADER_HEIGHT + 2 * ZONE_PADDING)

            zone_x = cursor_x
            zone_y = cursor_y

            for i, cname in enumerate(zone_comps):
                cx = zone_x + ZONE_PADDING
                cy = (zone_y + ZONE_HEADER_HEIGHT + ZONE_PADDING
                      + i * (COMP_HEIGHT + COMP_GAP_V))
                comp_positions[cname] = (cx, cy)
                placed.add(cname)

            zone_rects.append({
                "name": zone_name, "x": zone_x, "y": zone_y,
                "w": inner_w, "h": inner_h,
                "color": zone_color, "bgcolor": zone_bg,
                "comp_names": zone_comps,
            })
            cursor_x += inner_w + ZONE_GAP
        else:
            # Stack components horizontally within the zone
            inner_w = (n * COMP_WIDTH + (n - 1) * COMP_GAP_H
                       + 2 * ZONE_PADDING)
            inner_h = COMP_HEIGHT + ZONE_HEADER_HEIGHT + 2 * ZONE_PADDING

            zone_x = cursor_x
            zone_y = cursor_y

            for i, cname in enumerate(zone_comps):
                cx = (zone_x + ZONE_PADDING
                      + i * (COMP_WIDTH + COMP_GAP_H))
                cy = zone_y + ZONE_HEADER_HEIGHT + ZONE_PADDING
                comp_positions[cname] = (cx, cy)
                placed.add(cname)

            zone_rects.append({
                "name": zone_name, "x": zone_x, "y": zone_y,
                "w": inner_w, "h": inner_h,
                "color": zone_color, "bgcolor": zone_bg,
                "comp_names": zone_comps,
            })
            cursor_y += inner_h + ZONE_GAP

    # Place ungrouped components after all zones
    ungrouped = [name for name in components if name not in placed]
    ungrouped_positions: Dict[str, tuple] = {}
    if ungrouped:
        if is_lr:
            ux = cursor_x
            uy = ZONE_PADDING
        else:
            ux = ZONE_PADDING
            uy = cursor_y

        for i, name in enumerate(ungrouped):
            if is_lr:
                ungrouped_positions[name] = (ux, uy + i * (COMP_HEIGHT + COMP_GAP_V))
            else:
                ungrouped_positions[name] = (ux + i * (COMP_WIDTH + COMP_GAP_H), uy)

    return {
        "zone_rects": zone_rects,
        "comp_positions": comp_positions,
        "ungrouped_positions": ungrouped_positions,
    }


# ---------------------------------------------------------------------------
# mxGraph XML builder
# ---------------------------------------------------------------------------

def _build_component_style(comp: Dict[str, Any]) -> str:
    """Build the mxGraph style string for a component cell."""
    ctype = comp.get("type", "service")
    shape_style = SHAPE_MAP.get(ctype, "rounded=1;")
    fill = FILL_MAP.get(ctype, "#F5F5F5")
    border = BORDER_MAP.get(ctype, "#333333")

    # Apply style overrides if present
    overrides = comp.get("style_overrides", {})
    if "fillColor" in overrides:
        fill = overrides["fillColor"]
    if "strokeColor" in overrides:
        border = overrides["strokeColor"]

    style = (
        f"{shape_style}"
        f"whiteSpace=wrap;html=1;"
        f"fillColor={fill};strokeColor={border};"
        f"fontFamily=Helvetica;fontSize=12;fontStyle=1;"
    )
    return style


def _build_zone_style(zone_rect: Dict[str, Any]) -> str:
    """Build the mxGraph style string for a zone swimlane."""
    color = zone_rect["color"]
    bgcolor = zone_rect["bgcolor"]
    return (
        f"swimlane;startSize={ZONE_HEADER_HEIGHT};"
        f"fillColor={bgcolor};strokeColor={color};"
        f"rounded=1;arcSize=8;strokeWidth=2;dashed=1;dashPattern=8 4;"
        f"fontFamily=Helvetica;fontSize=13;fontStyle=1;"
        f"collapsible=1;container=1;"
    )


def _build_edge_style(flow: Dict[str, Any], default_routing: str) -> str:
    """Build the mxGraph style string for a flow edge."""
    routing = flow.get("style", default_routing)
    base = EDGE_STYLE_MAP.get(routing, EDGE_STYLE_MAP["orthogonal"])
    direction = flow.get("dir", "")

    style = (
        f"{base}"
        f"html=1;strokeColor=#666666;strokeWidth=1.5;"
        f"fontFamily=Helvetica;fontSize=10;"
    )

    if direction == "both":
        style += "startArrow=classic;endArrow=classic;startFill=1;endFill=1;"

    return style


def build_page_xml(
    page_desc: Dict[str, Any],
    page_name: str,
    ids: IdAllocator,
    layout_direction: str,
    h_spacing: int,
    v_spacing: int,
    default_edge_routing: str,
) -> ET.Element:
    """Build a single <diagram> element (one page in the .drawio file)."""

    diagram = ET.SubElement(ET.Element("tmp"), "diagram")
    diagram.set("name", page_name)
    diagram.set("id", ids.next())

    mx_model = ET.SubElement(diagram, "mxGraphModel")
    mx_model.set("dx", "1326")
    mx_model.set("dy", "846")
    mx_model.set("grid", "1")
    mx_model.set("gridSize", "10")
    mx_model.set("guides", "1")
    mx_model.set("tooltips", "1")
    mx_model.set("connect", "1")
    mx_model.set("arrows", "1")
    mx_model.set("fold", "1")
    mx_model.set("page", "1")
    mx_model.set("pageScale", "1")
    mx_model.set("math", "0")
    mx_model.set("shadow", "0")

    root = ET.SubElement(mx_model, "root")

    # Cell 0: root
    cell0 = ET.SubElement(root, "mxCell")
    cell0.set("id", "0")

    # Cell 1: default layer
    cell1 = ET.SubElement(root, "mxCell")
    cell1.set("id", "1")
    cell1.set("parent", "0")

    # Parse page contents
    components_list = page_desc.get("components", [])
    components = {c["name"]: c for c in components_list}
    zones = page_desc.get("zones", [])
    flows = page_desc.get("flows", [])

    # Validate flows reference existing components
    comp_names = set(components.keys())
    for flow in flows:
        for endpoint in ("from", "to"):
            name = flow.get(endpoint, "")
            if name and name not in comp_names:
                print(f"  Warning: flow references unknown component '{name}'",
                      file=sys.stderr)

    # Compute layout
    layout = _compute_zone_layout(
        zones, components, layout_direction, h_spacing, v_spacing
    )

    zone_rects = layout["zone_rects"]
    comp_positions = layout["comp_positions"]
    ungrouped_positions = layout["ungrouped_positions"]

    # Map component name → mxCell ID for edge wiring
    comp_cell_ids: Dict[str, str] = {}

    # --- Create zone swimlanes and their child components ---
    for zr in zone_rects:
        zone_id = ids.next()
        zone_cell = ET.SubElement(root, "mxCell")
        zone_cell.set("id", zone_id)
        zone_cell.set("value", zr["name"])
        zone_cell.set("style", _build_zone_style(zr))
        zone_cell.set("vertex", "1")
        zone_cell.set("parent", "1")

        geo = ET.SubElement(zone_cell, "mxGeometry")
        geo.set("x", str(zr["x"]))
        geo.set("y", str(zr["y"]))
        geo.set("width", str(zr["w"]))
        geo.set("height", str(zr["h"]))
        geo.set("as", "geometry")

        # Child components (parented to zone)
        for cname in zr["comp_names"]:
            comp = components.get(cname)
            if not comp:
                continue
            cid = ids.next()
            comp_cell_ids[cname] = cid

            label = comp.get("label", cname).replace("\n", "<br>")

            ccell = ET.SubElement(root, "mxCell")
            ccell.set("id", cid)
            ccell.set("value", label)
            ccell.set("style", _build_component_style(comp))
            ccell.set("vertex", "1")
            ccell.set("parent", zone_id)

            # Position relative to zone
            abs_x, abs_y = comp_positions.get(cname, (0, 0))
            rel_x = abs_x - zr["x"]
            rel_y = abs_y - zr["y"]

            cgeo = ET.SubElement(ccell, "mxGeometry")
            cgeo.set("x", str(rel_x))
            cgeo.set("y", str(rel_y))
            cgeo.set("width", str(COMP_WIDTH))
            cgeo.set("height", str(COMP_HEIGHT))
            cgeo.set("as", "geometry")

    # --- Ungrouped components (parented to layer 1) ---
    for cname, (ux, uy) in ungrouped_positions.items():
        comp = components.get(cname)
        if not comp:
            continue
        cid = ids.next()
        comp_cell_ids[cname] = cid

        label = comp.get("label", cname).replace("\n", "<br>")

        ucell = ET.SubElement(root, "mxCell")
        ucell.set("id", cid)
        ucell.set("value", label)
        ucell.set("style", _build_component_style(comp))
        ucell.set("vertex", "1")
        ucell.set("parent", "1")

        ugeo = ET.SubElement(ucell, "mxGeometry")
        ugeo.set("x", str(ux))
        ugeo.set("y", str(uy))
        ugeo.set("width", str(COMP_WIDTH))
        ugeo.set("height", str(COMP_HEIGHT))
        ugeo.set("as", "geometry")

    # --- Flow edges ---
    for flow in flows:
        src_name = flow.get("from", "")
        tgt_name = flow.get("to", "")
        src_id = comp_cell_ids.get(src_name)
        tgt_id = comp_cell_ids.get(tgt_name)

        if not src_id or not tgt_id:
            continue

        eid = ids.next()
        label = flow.get("label", "")

        ecell = ET.SubElement(root, "mxCell")
        ecell.set("id", eid)
        ecell.set("value", label)
        ecell.set("style", _build_edge_style(flow, default_edge_routing))
        ecell.set("edge", "1")
        ecell.set("source", src_id)
        ecell.set("target", tgt_id)
        ecell.set("parent", "1")

        egeo = ET.SubElement(ecell, "mxGeometry")
        egeo.set("relative", "1")
        egeo.set("as", "geometry")

    return diagram


def generate_drawio(
    description: Dict[str, Any],
    layout_override: Optional[str] = None,
    edge_routing_override: Optional[str] = None,
) -> str:
    """Generate a complete .drawio XML string from a description dict.

    Supports both single-page (root-level zones/components/flows) and
    multi-page (pages[] array) input formats.
    """
    ids = IdAllocator()

    # Resolve layout settings
    layout_cfg = description.get("layout", {})
    direction = layout_override or layout_cfg.get("direction", "LR")
    spacing = layout_cfg.get("spacing", {})
    h_spacing = spacing.get("horizontal", 200)
    v_spacing = spacing.get("vertical", 150)
    edge_routing = (edge_routing_override
                    or layout_cfg.get("edge_routing", "orthogonal"))

    title = description.get("title", "System Architecture")

    # Determine pages
    pages = description.get("pages", [])
    if not pages:
        # Single-page shorthand: treat root-level fields as one page
        pages = [{
            "name": title,
            "zones": description.get("zones", []),
            "components": description.get("components", []),
            "flows": description.get("flows", []),
        }]

    # Build XML
    mxfile = ET.Element("mxfile")
    mxfile.set("host", "app.diagrams.net")
    mxfile.set("type", "device")

    for page_desc in pages:
        page_name = page_desc.get("name", "Page")
        diagram = build_page_xml(
            page_desc, page_name, ids,
            direction, h_spacing, v_spacing, edge_routing,
        )
        mxfile.append(diagram)

    # Serialize to string with XML declaration
    ET.indent(mxfile, space="  ")
    xml_bytes = ET.tostring(mxfile, encoding="unicode", xml_declaration=False)
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_bytes


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def load_description(json_path: str) -> Optional[Dict[str, Any]]:
    """Load architecture description from a JSON file."""
    try:
        with open(json_path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: file not found: {json_path}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON: {e}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate editable draw.io diagrams from JSON architecture descriptions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Component types: client, service, database, external, gateway, ai, queue, cache, message

Layout directions: LR (left-to-right), TB (top-to-bottom)
Edge routing: orthogonal (default), curved, straight

Usage examples:
  %(prog)s -d arch.json -o diagram.drawio
  %(prog)s -d arch.json -o diagram.drawio --layout TB --edge-routing curved
        """,
    )
    parser.add_argument("-d", "--description", required=True,
                        help="JSON description file")
    parser.add_argument("-o", "--output", required=True,
                        help="Output .drawio file path")
    parser.add_argument("--layout", choices=["LR", "TB"], default=None,
                        help="Layout direction (overrides JSON)")
    parser.add_argument("--edge-routing",
                        choices=["orthogonal", "curved", "straight"],
                        default=None,
                        help="Edge routing style (overrides JSON)")

    args = parser.parse_args()

    description = load_description(args.description)
    if not description:
        sys.exit(1)

    comps = description.get("components", [])
    flows = description.get("flows", [])
    pages = description.get("pages", [])
    print(f"Loaded {len(comps)} components, {len(flows)} flows"
          + (f", {len(pages)} pages" if pages else ""))

    # Ensure output ends in .drawio
    output = args.output
    if not output.lower().endswith(".drawio"):
        output = output.rsplit(".", 1)[0] + ".drawio" if "." in output else output + ".drawio"

    xml_content = generate_drawio(
        description,
        layout_override=args.layout,
        edge_routing_override=args.edge_routing,
    )

    Path(output).parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        f.write(xml_content)

    print(f"Generated draw.io diagram: {output}")
    print("Open in draw.io desktop or https://app.diagrams.net to view and edit.")


if __name__ == "__main__":
    main()
