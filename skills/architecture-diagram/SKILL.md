---
name: architecture-diagram
description: >
  Generate editable draw.io (.drawio) architecture diagrams from structured JSON
  descriptions. Produces mxGraph XML files that open in draw.io desktop or web
  (app.diagrams.net). Supports zones, typed components, labelled data flows,
  multi-page diagrams, and configurable layout direction and edge routing.
license: Proprietary
triggers:
  - "architecture diagram"
  - "draw.io diagram"
  - "drawio diagram"
  - "create diagram"
  - "generate architecture"
  - "system diagram"
---

# Architecture Diagram Generator (draw.io)

Generate professional, **editable** architecture diagrams as `.drawio` files from structured JSON descriptions.

## Overview

This skill produces draw.io-compatible XML files that users can:
- Open in [draw.io desktop](https://github.com/jgraph/drawio-desktop) or [app.diagrams.net](https://app.diagrams.net)
- Refine layout by dragging components and zones
- Export to PNG, SVG, PDF from within draw.io
- Version-control as XML in git repositories

**Output:** A `.drawio` file with zone containers, typed component shapes, colour-coded nodes, and labelled data-flow edges.

## When to Use This Skill

**Use when the user asks to:**
- Create an architecture diagram, system diagram, or component diagram
- Generate a draw.io or drawio file
- Visualise system components, data flows, or infrastructure
- Create an editable version of an architecture overview

**Do NOT use when:**
- The user wants a Graphviz/DOT/PNG diagram → use `scope-document-generator` (Phase 4)
- The user wants a sequence diagram or flowchart → suggest Mermaid or PlantUML
- The user wants to edit an existing `.drawio` file → open it in draw.io directly

## Workflow

### Phase 1 — Input Collection

Ask the user for the architecture information. You need:

1. **Components**: What systems/services exist? What type is each? (see Component Types below)
2. **Zones**: How are components grouped? (e.g., "Cloud", "On-Premise", "Client Network")
3. **Data flows**: What connects to what? With what labels?
4. **Layout preference** (optional): Left-to-right (LR) or top-to-bottom (TB)?
5. **Edge routing** (optional): Orthogonal (default), curved, or straight?

If the user provides unstructured text, extract the architecture from it. If they provide an existing JSON description (e.g., from the Graphviz skill), use it directly — the format is backward compatible.

### Phase 2 — JSON Construction & Validation

Build the architecture description JSON following the schema below. Before generating:

1. **Read** `references/anti-hallucination-rules.md` — every component and flow must trace to user input
2. **Validate** all flow endpoints reference existing component names
3. **Verify** no components are orphaned (every component should be in a zone or have a flow)
4. Write the JSON to a temporary file (e.g., `/tmp/arch_desc.json`)

### Phase 3 — Diagram Generation

Run the generation script:

```bash
python skills/architecture-diagram/scripts/generate_drawio_diagram.py \
  -d /tmp/arch_desc.json \
  -o <workspace_folder>/architecture_diagram.drawio \
  --layout LR \
  --edge-routing orthogonal
```

**Output path:** Always write the `.drawio` file directly to the user's workspace/project folder (not `/tmp/`). This ensures Cowork can serve it as a downloadable file. The JSON description can live in `/tmp/` since it's an intermediate artifact.

CLI options:
| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `-d` / `--description` | file path | (required) | JSON description file |
| `-o` / `--output` | file path | (required) | Output `.drawio` path |
| `--layout` | `LR`, `TB` | `LR` | Layout direction |
| `--edge-routing` | `orthogonal`, `curved`, `straight` | `orthogonal` | Edge routing mode |

### Phase 4 — Delivery

1. Confirm the `.drawio` file was created successfully (check the script's exit code and stdout)
2. **Copy to workspace folder** and provide download link — save the `.drawio` file to the user's project/workspace directory (not `/tmp/`) so Cowork can serve it as a downloadable file
3. Tell the user:
   - The output file path
   - How to open it: "Open in draw.io desktop or https://app.diagrams.net → File > Open from > Device"
   - That they can drag-adjust positions and export to PNG/SVG/PDF
4. If the diagram has issues, iterate on the JSON and regenerate

**IMPORTANT — Do NOT attempt to open the file:**
- Do NOT run `open`, `xdg-open`, or any system command to launch the file
- Do NOT attempt to install draw.io or any other application
- The `.drawio` file is the deliverable — the user will open it on their own machine
- Simply provide the file path and opening instructions

## JSON Input Schema

### Minimal Example (backward compatible with Graphviz)

```json
{
  "title": "System Architecture",
  "zones": [
    {
      "name": "Cloud",
      "color": "#0078D4",
      "components": ["API Gateway", "Backend Service"]
    }
  ],
  "components": [
    {"name": "API Gateway", "type": "gateway"},
    {"name": "Backend Service", "type": "service"},
    {"name": "Database", "type": "database"}
  ],
  "flows": [
    {"from": "API Gateway", "to": "Backend Service", "label": "REST API"},
    {"from": "Backend Service", "to": "Database", "label": "Read/Write"}
  ]
}
```

### Full Schema (with draw.io extensions)

```json
{
  "title": "System Architecture",
  "layout": {
    "direction": "LR",
    "spacing": {
      "horizontal": 200,
      "vertical": 150
    },
    "edge_routing": "orthogonal"
  },
  "zones": [
    {
      "name": "Azure Virtual Network",
      "color": "#0078D4",
      "bgcolor": "#E6F2FF",
      "components": ["VPN Gateway", "Pipeline"]
    }
  ],
  "components": [
    {
      "name": "SQL Database",
      "type": "database",
      "label": "SQL\nDatabase",
      "description": "Main data store",
      "style_overrides": {
        "fillColor": "#D4EDDA",
        "strokeColor": "#155724"
      }
    }
  ],
  "flows": [
    {
      "from": "SQL Database",
      "to": "VPN Gateway",
      "label": "Load data",
      "dir": "both",
      "style": "orthogonal"
    }
  ],
  "pages": [
    {
      "name": "Overview",
      "zones": [],
      "components": [],
      "flows": []
    },
    {
      "name": "Detail View",
      "zones": [],
      "components": [],
      "flows": []
    }
  ]
}
```

### Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `title` | No | Diagram title (used as page name for single-page) |
| `layout` | No | Layout configuration object |
| `layout.direction` | No | `"LR"` (left-to-right) or `"TB"` (top-to-bottom). Default: `"LR"` |
| `layout.spacing.horizontal` | No | Horizontal spacing in pixels. Default: `200` |
| `layout.spacing.vertical` | No | Vertical spacing in pixels. Default: `150` |
| `layout.edge_routing` | No | `"orthogonal"`, `"curved"`, or `"straight"`. Default: `"orthogonal"` |
| `zones[].name` | Yes | Display name for the zone container |
| `zones[].color` | No | Border colour (hex). Default: `#999999` |
| `zones[].bgcolor` | No | Background colour (hex). Auto-lightened from `color` if omitted |
| `zones[].components` | Yes | List of component names in this zone |
| `components[].name` | Yes | Unique component name (used for flow references) |
| `components[].type` | No | Component type (see table below). Default: `"service"` |
| `components[].label` | No | Display label (supports `\n` for line breaks). Default: component name |
| `components[].description` | No | Tooltip description (stored in draw.io metadata) |
| `components[].style_overrides` | No | Override `fillColor` and/or `strokeColor` |
| `flows[].from` | Yes | Source component name |
| `flows[].to` | Yes | Target component name |
| `flows[].label` | No | Edge label text |
| `flows[].dir` | No | `"both"` for bidirectional arrows |
| `flows[].style` | No | Per-edge routing override: `"orthogonal"`, `"curved"`, `"straight"` |
| `pages[]` | No | Array of page objects for multi-page diagrams |
| `pages[].name` | Yes | Page/tab name in draw.io |

### Component Types

| Type | draw.io Shape | Fill Colour | Border Colour | Use For |
|------|--------------|-------------|---------------|---------|
| `client` | Rounded rectangle | `#E1F5FF` | `#01579B` | Web apps, mobile apps, user interfaces |
| `service` | Rounded rectangle | `#F3E5F5` | `#4A148C` | Backend services, microservices, APIs |
| `database` | Cylinder | `#E8F5E9` | `#1B5E20` | Databases, data stores, data warehouses |
| `external` | Component shape | `#FFF3E0` | `#E65100` | External systems, third-party services |
| `gateway` | 3D box | `#F3E5F5` | `#4A148C` | API gateways, VPN gateways, load balancers |
| `ai` | Hexagon | `#E3F2FD` | `#0D47A1` | ML models, AI services, LLM endpoints |
| `queue` | Parallelogram | `#F1F8E9` | `#33691E` | Message queues, event streams, buffers |
| `cache` | Octagon | `#FCE4EC` | `#880E4F` | Cache layers, CDNs, in-memory stores |
| `message` | Message shape | `#FCE4EC` | `#880E4F` | Email, notifications, messaging services |

### Multi-Page Diagrams

Use the `pages[]` array when you need multiple views (e.g., overview + detail, logical + physical). Each page has its own `zones`, `components`, and `flows`. Root-level `zones`/`components`/`flows` are treated as a single-page shorthand when `pages` is absent or empty.

```json
{
  "title": "System Architecture",
  "pages": [
    {
      "name": "High-Level Overview",
      "zones": [...],
      "components": [...],
      "flows": [...]
    },
    {
      "name": "Data Flow Detail",
      "zones": [...],
      "components": [...],
      "flows": [...]
    }
  ]
}
```

## File Paths

All paths are relative to the plugin root (`docs-generator/`):

```
skills/architecture-diagram/
├── SKILL.md                                    # This file
├── scripts/
│   └── generate_drawio_diagram.py              # Core diagram generator
└── references/
    └── anti-hallucination-rules.md             # Read before generating content
```

## Content Quality Standards

1. **Every component must trace to user input** — do not invent systems that weren't mentioned
2. **Every flow must connect existing components** — the script warns about unknown references
3. **Use exact terminology from the user** — do not rename services or rephrase labels
4. **Flag gaps explicitly** — if the user's description is incomplete, ask rather than assume
5. **Keep it simple** — include only what was discussed; recommend additional components for "Phase 2"
