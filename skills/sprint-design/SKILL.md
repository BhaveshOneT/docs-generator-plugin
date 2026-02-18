---
name: sprint-design
description: >
  Generate concise, client-focused Project Design Plan pages directly in Confluence.
  Triggers on: "design plan", "sprint design", "project design plan",
  "sprint plan", "create design plan", "generate sprints",
  "project timeline", "sprint breakdown", "design plan for this".
  Transforms hackathon summaries and customer conversation inputs into
  structured Confluence pages with architecture diagram and sprint
  timeline table — placed under the correct use-case → project
  management → project design plan hierarchy. Section inclusion follows
  deterministic rules based on sprint count, source material, and
  project complexity. Supports English and German. Includes confidence
  scoring and smart Confluence/Close CRM lookup for missing metadata.
license: Proprietary
triggers:
  - "design plan"
  - "sprint design"
  - "project design plan"
  - "sprint plan"
  - "create design plan"
  - "generate sprints"
  - "project timeline"
  - "sprint breakdown"
  - "design plan for this"
  - "sprint design for this"
  - "create sprints"
  - "timeline and sprints"
---

# Sprint Design (Project Design Plan) Skill

## Overview

This skill generates **Project Design Plan** pages directly in Confluence, following the established One Thousand 2025+ structure. It takes up to three inputs — a hackathon summary document, a scope document (when available), and additional customer conversation context — and produces a **concise, client-focused** design plan with architecture diagram and sprint timeline table.

The workflow: Collect inputs (hackathon doc + scope doc + customer notes) → Extract content → Apply deterministic section rules → Score confidence → Fill metadata gaps from Close CRM (dates, names only) → Ask user for remaining gaps → Generate architecture diagram → Publish to Confluence → Instruct user to upload diagram manually → Verify.

**Output:** A Confluence page published under `[Use Case Space] → Project Management → Project Design Plan` with markdown-formatted content, architecture diagram placeholder (user uploads manually), and structured sprint table. Section inclusion is determined by hard IF/THEN rules (see Rule 2) — not left to judgment.

**Source authority hierarchy for sprint content:**
1. **Scope document** — authoritative for sprint count, sprint goals, sprint durations, and in/out-of-scope features. When a scope doc exists, use its sprint breakdown directly — do NOT re-derive sprints from the hackathon doc.
2. **Hackathon summary** — authoritative for technical architecture, use case background, data sources, and component details.
3. **Additional input from user** — authoritative for anything not covered in the two documents: follow-up decisions, updated timelines, scope changes, or client preferences.

---

## ⚠️ CRITICAL: Conciseness & Format Rules

**These rules are NON-NEGOTIABLE.** They are derived from analysis of all 2025+ OT design plans in Confluence (Yellow Bikes Jan'25, Blue Homes UC2 Mar'25, Colorful-Toys Oct'25, MICUBO Dec'25). Pre-2025 designs are excluded as they use outdated patterns. Violating these creates documents that look nothing like current OT deliverables.

### Rule 1: Length Discipline (450–2000 words depending on complexity)
- **Simple (2-3 sprints):** 400-550 words. Reference: Colorful-Toys (~450).
- **Medium (4-6 sprints):** 550-800 words. Reference: Yellow Bikes (~550), Blue Homes UC2 (~700).
- **Complex (7+ sprints):** 1500-2000 words. Reference: MICUBO (~2000).
- More data from enrichment sources does NOT mean more content. Write smarter, not longer.
- Every sentence must earn its place. If removing a sentence doesn't lose actionable information, remove it.
- The Timeline table is always the largest section. If the page is getting long, cut from OTHER sections — never shorten the timeline table.

### Rule 2: Section Inclusion Rules (Deterministic — NO Guesswork)
Based on analysis of all 2025+ OT design plans (Yellow Bikes Jan'25, Blue Homes UC2 Mar'25, Colorful-Toys Oct'25, MICUBO Dec'25). Every section has a hard IF/THEN rule — follow it exactly.

**ALWAYS INCLUDE (present in 4/4 designs):**
- `## Initial Architecture` — image only by default. Add a 1-sentence intro ONLY IF the architecture is described as "still needs refinement" in source. Add `## Updated Architecture` ONLY IF the source shows the architecture evolved during planning. NEVER write text descriptions of the architecture.
- `## Timeline & Design` (or `## Timeline and Design` / `## Timeline & Sprints`) — sprint table with 4 columns by default. See Rule 5 for when to use 5 columns. This is THE core deliverable.

**CONDITIONAL sections — each has a specific trigger:**

| Section | INCLUDE when | SKIP when |
|---------|-------------|-----------|
| **Opening (OT intro)** | Source has enough to fill the template (client name, use case, timeline, sprint count, benefit) | Source lacks 2+ of these values AND project is simple (≤3 sprints) |
| **`## Overview`** | Project is complex (7+ sprints) OR product is novel and needs explaining | Project is simple/medium and context is clear |
| **`## Key Requirements`** | No scope document exists for this project AND requirements are present in source material | A scope document already exists (check Confluence) |
| **`## Notes & Dependencies`** | 1-3 critical external dependencies exist that are NOT already captured in Key Requirements or Timeline table epics | Dependencies are already in Key Reqs bullets or Timeline epics, OR no external dependencies discussed |
| **`## Sprint Plan Overview`** | 7+ sprints | Fewer than 7 sprints (3/4 designs skip this) |
| **`## Design Decisions`** | Source material explicitly discusses 1-3 specific technical decisions | No explicit technical decisions discussed in source |

**Opening is ONE of three styles — pick based on conditions above:**
- Style A (OT Template): Use when source has enough values for the template. See Rule 3.
- Style B (`## Overview`): Use when 7+ sprints OR product needs explaining.
- Style C (No opening): Use when ≤3 sprints AND context is already clear. Jump to Key Requirements or Architecture.
- If BOTH Style A and B conditions are met, use Style B (it's more informative).

**NEVER INCLUDE (0/4 in 2025+ designs):**
- `## Effort Estimation` as a separate section — eliminated in all 2025+ designs. If client effort was discussed, put it in the timeline table's 5th column (see Rule 5).
- Sprint 0 — all 2025+ designs start at Sprint 1.
- `## Architecture` with text description — originals have only an image, never prose.
- Appendix, Source Traceability, Known Unknowns — never present in any design.
- OT Team Effort or internal resource allocation.

### Rule 3: Standard OT Introduction Template
When Rule 2 selects Style A (OT Template), use this exact pattern (adapt bracketed values):

```
Welcome to our project design plan aimed at developing a **minimum viable product** tailored for [use case description]. Within **a [N]-week timeline**, structured into [N] [duration] sprints, our primary focus is on seamlessly integrating [a] functional AI application[s] into **[Client Name]'s system**. This integration will empower users with [key benefit], enhancing operational efficiency.

Let's embark on this journey to create a robust solution that meets the evolving needs of [Client Name] and its [team/customers].
```

### Rule 4: NO Separate Effort Estimation Section (2025+ Standard)
- A separate `## Effort Estimation` section does NOT appear in ANY 2025+ design plan (0/4).
- If client effort was discussed in source material, it goes in the timeline table as a 5th column (see Rule 5) — NOT as a separate section.
- If client effort was NOT discussed, use the 4-column table and do not mention effort at all.
- **NEVER** list One Thousand team effort, FTE weeks, or internal resource allocation anywhere in the document.

### Rule 5: Timeline Table Columns
The timeline table is the core deliverable. Column structure varies by project:

**4-column format (MICUBO, Colorful-Toys pattern — most common):**
```
| Sprint | Timeline | Goal | Epics (high level features) |
```

**5-column format (Blue Homes pattern — when client effort is discussed):**
```
| Sprint | Timeline | Goal | Epics (high level features) | Estimated invest from [Client] (in persondays) |
```

Include the client effort column ONLY when effort data was explicitly discussed in source material. If it wasn't discussed, use the 4-column format — don't invent effort estimates.

- Epics use category prefixes: **Data:**, **AI:**, **Pipeline:**, **Integration:**, **Testing:**, **Documentation:**, **Scope:**, **Deployment:**
- Release event row: Include ONLY IF the source material explicitly mentions a release milestone or go-live date. Otherwise omit (only 1/4 of 2025+ designs has it).
- All sprints start at Sprint 1 — NEVER use Sprint 0 (0/4 in 2025+ designs).

### Rule 6: Architecture Diagram — Manual Upload Required
- The Confluence MCP tools do NOT support image/attachment uploads.
- Generate the diagram PNG via Graphviz and save to workspace folder.
- In the Confluence page, include placeholder: `**[Architecture diagram to be added — PNG file provided separately]**`
- **MANDATORY:** At the END of every conversation where a design plan is created, ALWAYS tell the user:
  > "Please upload the architecture diagram PNG to the Confluence page by editing the page and dragging the image into the Architecture section."
- This instruction must be given EVERY TIME. Do not skip it. Do not assume the user knows.

### Rule 7: Enrichment Discipline + Temporal Awareness

**PRIMARY CONTENT SOURCES — ranked by authority:**

1. **Scope document** — THE authoritative source for sprint structure. When a scope doc is provided or found in Confluence, extract from it:
   - Sprint count, sprint names, sprint goals (use verbatim from scope doc — do not paraphrase)
   - Sprint durations (scope docs specify which sprints are 1-week, 2-week, refinement, etc.)
   - In-scope and out-of-scope features (drives which epics appear in which sprints)
   - Client prerequisites and pre-sprint decisions
   - Go-live / release date (if mentioned)
   - **Do NOT re-derive sprint structure from the hackathon doc when a scope doc exists.**

2. **Hackathon summary document** — authoritative for technical content that predates the scope doc:
   - Use case background and business context
   - Architecture components and data flows
   - Data sources and infrastructure details
   - Technical approach and technologies used

3. **Customer conversation / additional input** — authoritative for decisions made after the hackathon:
   - Updated requirements or scope changes
   - Timeline adjustments
   - New dependencies or prerequisites

**SECONDARY SOURCES (Confluence project pages, Close CRM, Miro, Jira) — for METADATA ONLY:**
These sources should ONLY be used to fill in missing metadata values:
- ✅ Client name, team names, stakeholder names
- ✅ Calendar weeks, project start dates, deal timelines
- ✅ Confluence space structure (to find the right parent page)
- ✅ Deal value, contract context (from Close CRM)

**NEVER pull content from secondary sources into sprint epics or goals:**
- ❌ PoC results, accuracy metrics, implementation findings
- ❌ Specific file names, tool choices, algorithm decisions discovered during work
- ❌ Status updates ([DONE], [WIP]) from completed sprints
- ❌ Post-hoc design decisions made during development
- ❌ Bug fixes, edge cases, or constraints discovered after planning

**WHY:** Confluence pages for an existing project contain data created DURING and AFTER sprint execution. A sprint design is written BEFORE work begins — it captures PLANNED work, not results. Pulling Confluence content into the sprint design creates a temporal mismatch where the plan contains information that wouldn't have existed at planning time.

**Rule of thumb:** If a piece of information would only be known AFTER sprints begin, do NOT include it. Use `[To be confirmed]` instead.

### Rule 8: Sprint Sequencing Logic
Sprints must follow a logical dependency chain. Sprint 1 (always the first sprint — never Sprint 0) should address alignment/setup before diving into development. Common anti-patterns to AVOID:
- **Do NOT** put feature development before resolving business alignment issues (e.g., accuracy expectations, scope).
- **Do NOT** put production hardening or monitoring before core functionality is refined.
- Each sprint's output should logically precede the next sprint's dependencies.
- Example logical flows:
  - **Simple:** Data setup → Core feature → Testing/UAT
  - **Medium:** Alignment → Refinement → New features → Integration testing → Handover
  - **Complex:** Alignment → Data layer → Core AI → Integration → Validation → UAT → Handover

### Rule 9: Minimize Duplicate Content Across Documents
The design plan exists alongside other project documents (hackathon summary, scope document). Duplication rules:
- Scope document exists → SKIP Key Requirements section (Rule 2 makes this deterministic).
- Scope document does NOT exist → INCLUDE Key Requirements section IF requirements are in source material (Rule 2).
- Architecture text descriptions → NEVER include (just the diagram image).
- The design plan's PRIMARY job is: architecture image + sprint timeline table. Everything else supports these two.

### Rule 10: Content Filtering — What Goes In vs What Stays Out
The hackathon doc and scope doc will contain FAR more detail than belongs in a design plan. A design plan is a HIGH-LEVEL PLAN, not a technical specification. Apply these filters to EVERY piece of source content before including it:

**INCLUDE in the design plan (feature-level):**
- ✅ What the system will do (capabilities, integrations, deliverables)
- ✅ Specific system/platform names from source (Azure, SAP, PXM, Teams)
- ✅ Client domain terms exactly as stated (Produktberater, Baugruppen)
- ✅ Quantified scope constraints from source (10 room types, 200 parallel calls)
- ✅ External dependencies the client must provide (data access, environments)
- ✅ Calendar weeks and timeline data

**FILTER OUT from the design plan (too granular or wrong temporal context):**
- ❌ Algorithm names/choices (unless the algorithm IS the feature)
- ❌ Specific file names, dataset names, table names
- ❌ PoC results, accuracy metrics, benchmark numbers
- ❌ Implementation-level tasks (refactoring, bug fixes, PR reviews)
- ❌ Individual person names (use roles: "IT team", "application team")
- ❌ Conditional logic or fallback plans
- ❌ Success criteria or KPIs
- ❌ Meeting schedules, process details, ceremony descriptions
- ❌ Cost estimates or pricing
- ❌ Risk registers or mitigation strategies
- ❌ Parenthetical rationale explaining WHY something is done
- ❌ Anything discovered or decided DURING sprint execution (temporal contamination)

**Test for each piece of content:** "Would someone writing a plan BEFORE work begins know this information?" If NO → filter it out.

**Detail level reference by section:**

| Section | Detail level | Words per item |
|---------|-------------|---------------|
| Key Requirements | Capability/constraint | 7-15 words/bullet |
| Notes & Dependencies | Deliverable/process | 11-17 words/bullet |
| Sprint Goal | Objective | 10-20 words |
| Sprint Epic item | Feature-level task | 5-18 words |
| Client Effort cell | Team + action | 20-30 words |
| Design Decision | Decision + context | 15-30 words |

---

## When to Use This Skill

**ALWAYS invoke this skill when the user's request matches ANY of these patterns:**

- User says "design plan", "sprint design", "project design plan", or "sprint plan"
- User wants to create sprints/timeline from a hackathon summary
- User wants to generate a "project design plan" in Confluence
- User has hackathon output and customer feedback and wants to plan sprints
- User says "create design plan for [project]" or similar

**Do NOT invoke for:** scope documents (use scope-document-generator), general Word docs, slide decks, or non-Confluence deliverables.

---

## CRITICAL: Safety Rules

### No Modification or Deletion of Existing Data

1. **NEVER modify** existing Confluence pages unless explicitly told to update a specific page
2. **NEVER delete** any Confluence pages, comments, or content
3. When publishing, **always create a NEW page** under the correct parent
4. If a "Project Design Plan" page already exists under the target parent, **ASK the user** before proceeding:
   - Option A: Create with a different title (e.g., "Project Design Plan v2" or "Project Design Plan - Updated")
   - Option B: Update the existing page (only with explicit user confirmation)
5. Before publishing, **always show the user a preview** of what will be created and where

### No Hallucination

All anti-hallucination rules from `references/anti-hallucination-rules.md` apply. Key summary:
- NEVER invent metrics, KPIs, timelines, or technical details
- EVERY claim must trace to hackathon document, scope document, or customer conversation
- Use `[To be confirmed]` / `[Noch zu bestätigen]` for unknowns
- NEVER add features, components, or sprints not discussed in source material
- NEVER assume sprint durations, team sizes, or effort estimates

---

## Inputs

This skill works with up to **three inputs**:

### Input 1: Scope Document *(primary for sprint structure)*
- Can be a PDF, DOCX, or text pasted in conversation
- **This is the authoritative source for:** sprint count, sprint names, sprint goals, sprint durations, in/out-of-scope features, client prerequisites, and release/go-live date
- When a scope doc is provided, use its sprint breakdown directly — do not invent or re-derive sprint structure from the hackathon doc
- If no scope doc is available, sprint structure must be derived from the hackathon doc and customer notes (mark sprint count as `[To be confirmed]` if uncertain)

### Input 2: Hackathon Summary Document *(primary for technical content)*
- Can be a PDF, DOCX, or text pasted in conversation
- **This is the authoritative source for:** use case background, architecture components, data sources, technologies, and business context
- Architecture diagrams are extracted from here (or the scope doc if it includes one)

### Input 3: Additional Input *(anything not in the two documents)*
- Anything the user wants reflected in the design plan that isn't already covered by the hackathon doc or scope document
- Examples: decisions made in follow-up calls, updated timelines, scope changes, client preferences, open questions raised after the hackathon
- Can be provided as free text — no specific format required
- **Priority:** This input overrides both the hackathon doc and scope doc when there are conflicts (flag the conflict to the user)

---

## Workflow

### Phase 1: Input Collection + Background Setup

Ask the user using AskUserQuestion:

1. **Language:** English or German?
2. **Confluence Space:** Which space should the design plan be created in? (Provide space key or name)
3. **Project/Use Case Name:** Name of the project (used for page title)
4. **Scope Document:** Do you have a scope document? (PDF, DOCX, or paste text) — this is where sprint structure comes from
5. **Hackathon Document:** Source file (PDF, DOCX, or text) — for technical background and architecture
6. **Additional Input:** Is there anything not covered in the hackathon or scope document that should be reflected in the design plan? (e.g. decisions made in follow-up calls, updated timelines, scope changes, client preferences) — optional, skip if not applicable
7. **Architecture Diagram:** Extract from source, generate new, or skip?

#### Background: Pre-warm Dependencies

**While waiting for user responses**, launch a background agent to install dependencies:

```bash
pip install pdfplumber python-docx Pillow graphviz --break-system-packages --quiet 2>/dev/null
which dot || echo "Graphviz not installed — will use Pillow fallback for diagrams"
```

---

### Phase 2: Confluence Navigation + Content Extraction

#### Step 2a: Find the Correct Parent Page

The design plan MUST be created under the correct hierarchy:
```
[Space Root]
  └── [Use Case / Project Name]
       └── Project Management
            └── Project Design Plan  ← CREATE HERE
```

**To find the parent:**

1. Use the Confluence MCP tools to search for "Project Management" pages in the target space:
   ```
   searchConfluenceUsingCql: title = "Project Management" AND space = "[SPACE_KEY]" AND type = page
   ```

2. If found, use that page's ID as the parent for the new design plan page.

3. If NOT found, ask the user:
   - "I couldn't find a 'Project Management' page in space [SPACE_KEY]. Should I create the page hierarchy, or place it somewhere else?"

4. Before creating, check if a "Project Design Plan" page already exists under that parent:
   ```
   getConfluencePageDescendants: pageId = [PROJECT_MANAGEMENT_PAGE_ID]
   ```
   If one exists, ask user whether to create a new version or update.

#### Step 2b: Smart Lookup for Missing METADATA Only

Before asking the user for missing metadata, search secondary sources. **Remember Rule 7: secondary sources are for METADATA only, not content.**

**What to look for (metadata):**
- Client name, team names, stakeholder roles
- Calendar weeks, project start/end dates
- Deal value, contract type (from Close CRM)
- Confluence space structure (to find parent page)
- Whether a scope document already exists in Confluence (if user didn't provide one)

**What NOT to pull from secondary sources (content):**
- Technical details, implementation specifics, PoC findings
- Sprint outcomes, status updates, bug fixes
- Specific tool choices, algorithm decisions, file names
- Anything that was created DURING or AFTER the project started

**Confluence searches (metadata only):**
1. If user did not provide a scope doc, search Confluence: `title ~ "scope" AND space = "[SPACE_KEY]"` → if found, fetch it and treat it as Input 1 (scope document)
2. Search for project management page: find correct parent for page placement

**Close CRM searches (if available):**
3. Search for the client lead: `lead_search: name = "[Client Name]"` → extract deal dates, value, timeline only

**All sprint content (epics, goals, requirements, architecture) must come from the scope doc, hackathon doc, or user input — NEVER from Confluence project pages that were created during the project.**

#### Step 2c: Content Extraction

**Read reference files in parallel** (use multiple Read tool calls in a single message):

- `references/anti-hallucination-rules.md` — what NOT to invent
- `references/design-plan-structure.md` — structure templates based on real examples

---

**From the scope document, extract (this is the sprint source of truth):**

1. **Sprint breakdown** — the complete list of sprints, verbatim:
   - Number of sprints and any refinement/pause phases
   - Name or goal of each sprint (use exact wording from scope doc)
   - Duration of each sprint (2-week, 1-week, etc.) — some scope docs specify different durations per sprint
   - Any go-live or release event explicitly mentioned
2. **In-scope features** — the confirmed feature list (drives epic content per sprint)
3. **Out-of-scope features** — explicitly excluded items (prevents hallucinating features)
4. **Client prerequisites** — what the client must deliver before the project starts
5. **Pre-project decisions** — open decisions the client must resolve before Sprint 1

If the scope doc contains a "High Level Sprint Design" or equivalent section, that section defines the sprint structure — use it directly, don't reinterpret it.

---

**From the hackathon document, extract:**

1. Project overview / business context
2. Technical approach / technologies used
3. Architecture components and data flows
4. Data sources and infrastructure details
5. Client effort expectations (if discussed — goes in table 5th column, not separate section)
6. Any sprint discussions that predate the scope doc (use only if no scope doc exists)

---

**From the user's additional input, extract:**

1. Anything not already covered by the hackathon doc or scope doc
2. Decisions made in follow-up calls, updated timelines, scope changes
3. New dependencies or prerequisites raised after the hackathon
4. Client preferences or open questions (flag any conflicts with the scope doc)

---

### Phase 3: Content Generation with Confidence Scoring

#### CRITICAL: Confidence Scoring System

After generating each section, Claude MUST self-assess a **confidence score (0–100)** based on five dimensions. This score is used internally to decide whether to ask the user for more input.

**Scoring Criteria per Section (each 0–20 points):**

1. **Source grounding (0–20):** Is every claim traceable to source? (20 = every sentence backed, 0 = entirely invented)
2. **Specificity (0–20):** Are names, tools, integrations specific? (20 = "GCP Firestore via REST API", 0 = "the database")
3. **Completeness (0–20):** Does the section cover its purpose fully? (20 = nothing missing, 0 = skeletal)
4. **Actionability (0–20):** Can someone act on this content? (20 = clear deliverables, 0 = hand-wavy)
5. **Anti-hallucination (0–20):** Is the section free of invented details? (20 = nothing fabricated, 0 = multiple fabrications)

**Section-specific minimum thresholds:**

| Section | Minimum Score | When scored |
|---------|--------------|-------------|
| Opening (Style A/B) | 70 | When Rule 2 includes an opening |
| Architecture (image) | 65 | Always (must exist) |
| Timeline & Design Table | 80 | Always (core deliverable — must be precise) |
| Key Requirements | 70 | When Rule 2 includes it (no scope doc exists) |

**Architecture and Timeline are always scored.** Opening and Key Requirements are scored only when Rule 2's conditions trigger their inclusion. Other conditional sections (Notes & Dependencies, Sprint Plan Overview, Design Decisions) are brief enough to not need formal scoring — just verify they're source-grounded.

#### Iterative Review Loop

After scoring all sections, if ANY section falls below its threshold:

1. **First: Check source documents again** — Re-read scope doc and hackathon doc for missed details. Check Close CRM for metadata (dates, names) only. Do NOT pull content from Confluence project pages (see Rule 7).

2. **Then: Show the user a summary table** (only include sections that are present in this plan):
   ```
   Section                    Score   Status
   ──────────────────────────────────────────
   Opening (Style A)           85     ✓ Pass
   Architecture                55     ✗ Needs input
   Timeline & Design           72     ✗ Needs input (below 80)
   Key Requirements            62     ✗ Needs input (included — no scope doc exists)
   ```

3. **For each failing section, ask specific questions.** Do NOT ask vague questions.

4. **Re-generate failing sections** with new input. **Do NOT make sections longer — make them more accurate.**
5. **Re-score** and repeat until all pass OR user says to proceed anyway.

**The user can always override** by saying "proceed anyway" — use `[To be confirmed]` markers on weak sections.

---

### Phase 4: Architecture Diagram Generation

Every design plan MUST include an architecture diagram (4/4 in 2025+ designs). Use the **same Graphviz-based approach** as the scope-document-generator skill.

#### Diagram Generation

The diagram generation script is shared with the scope skill. Reference it at:
```
../scope-document-generator/scripts/generate_architecture_diagram.py
```

Or use the local copy at:
```
scripts/generate_architecture_diagram.py
```

**Usage:**
```bash
SKILL_DIR="[path-to-sprint-design-skill]"

python "$SKILL_DIR/scripts/generate_architecture_diagram.py" \
  --description /tmp/arch_desc.json \
  --output /tmp/arch_diagram.png \
  --style detailed
```

**Description JSON format:**
```json
{
  "title": "System Architecture",
  "zones": [
    {
      "name": "Client Infrastructure",
      "components": ["PXM System", "SAP", "Web Portal"]
    },
    {
      "name": "Azure / GCP Environment",
      "color": "#0078D4",
      "components": ["AI Service", "Vector DB", "API Gateway", "Chat Interface"]
    }
  ],
  "components": [
    {"name": "PXM System", "type": "external"},
    {"name": "SAP", "type": "database"},
    {"name": "AI Service", "type": "ai"},
    {"name": "Vector DB", "type": "database"},
    {"name": "API Gateway", "type": "gateway"}
  ],
  "flows": [
    {"from": "PXM System", "to": "AI Service", "label": "Product data"},
    {"from": "AI Service", "to": "Vector DB", "label": "Embeddings"}
  ]
}
```

**Component types → shapes:** `client` (rounded box), `service` (rounded box), `database` (cylinder), `external` (component), `gateway` (3D box), `ai` (double octagon), `queue`, `cache`, `message`

**Rendering pipeline (automatic fallback):**
1. **Graphviz `dot`** — primary renderer
2. **Pillow PNG** — basic grid fallback

#### ⚠️ Uploading Diagram to Confluence (MANUAL STEP)

The Confluence MCP tools do NOT support file/attachment uploads. This is a known limitation.

**Required workflow:**
1. Generate the diagram PNG and save to workspace folder
2. In the Confluence page body, include: `**[Architecture diagram to be added — PNG file provided separately]**`
3. Provide the PNG file to the user via: `[View diagram](computer:///sessions/.../arch_diagram.png)`
4. **MANDATORY end-of-conversation instruction to user:**
   > "Please upload the architecture diagram to the Confluence page: edit the page → drag the PNG into the Architecture section → save."

**This instruction MUST be given at the end of EVERY design plan creation. Never skip it.**

---

### Phase 5: Confluence Page Generation

#### Design Plan Structure

Based on analysis of **all 2025+ OT design plan pages**. Each section's inclusion is governed by Rule 2's deterministic conditions — follow them exactly.

```markdown
[IF Rule 2 selects Style A → OT intro paragraph, no heading]
[IF Rule 2 selects Style B → ## Overview with 2-3 paragraphs]
[IF Rule 2 selects Style C → skip opening entirely]

## Key Requirements                    ← IF no scope doc exists AND requirements in source
- [requirement 1]
- [requirement 2]
- [5-8 bullets total, 1-2 sentences each]

## Notes & Dependencies               ← IF 1-3 critical dependencies NOT in Key Reqs or Timeline epics
- **[Label]:** [dependency description]
- [2-3 bullets max]

## Initial Architecture                ← ALWAYS
**[Architecture diagram to be added — PNG file provided separately]**

## Updated Architecture                ← IF source shows architecture evolved during planning
**[Updated diagram to be added]**

## Sprint Plan Overview                ← IF 7+ sprints
- **Sprint 1:** [one-line summary]
- **Sprint 2:** [one-line summary]

## Timeline & Design                   ← ALWAYS (core deliverable)

4-column (default) or 5-column (IF client effort was explicitly discussed — see Rule 5):

| **Sprint** | **Timeline** | **Goal** | **Epics (high level features)** |
| --- | --- | --- | --- |
| Sprint 1 | CW X–Y | [Goal] | **Category:** [planned tasks] |
| Sprint 2 | CW X–Y | [Goal] | **Category:** [planned tasks] |
| ... | ... | ... | ... |
| Release event | CW XX | | Yay 🎉 🥂 🎈 | ← IF source explicitly mentions release milestone

## Design Decisions                    ← IF 1-3 explicit tech decisions discussed in source
- [decision 1]
```

**Typical plans use 2-3 sections** (Architecture + Timeline, sometimes with an opening or Key Requirements). NEVER include: Effort Estimation as separate section, Sprint 0, Architecture text descriptions, Appendix, Source Traceability, Known Unknowns, OT Team Effort.

#### Content Format

Generate the page content as **markdown** (Confluence API supports markdown format). Use:
- `##` for main section headings (standard; `###` is also acceptable — be consistent within the document)
- `###` for sub-headings (sparingly)
- `|` pipe tables for the timeline
- `*` or `-` for bullet lists
- `**bold**` for emphasis

#### Publishing to Confluence

Use the Confluence MCP tool to create the page:

```
createConfluencePage:
  cloudId: [from getAccessibleAtlassianResources]
  spaceId: [target space ID]
  parentId: [Project Management page ID]
  title: "Project Design Plan"  (or "[Project Name] - Design Plan")
  body: [generated markdown content]
  contentFormat: "markdown"
```

**IMPORTANT:** Always show the user the content preview BEFORE publishing. Ask for explicit confirmation:
- "Here's the design plan I've prepared. Should I publish it to Confluence under [Space] → Project Management → Project Design Plan?"

#### Retrieving the Page URL

After successful creation, the `createConfluencePage` MCP tool returns the page ID. Construct the URL:
```
https://leadmachinelearning.atlassian.net/wiki/spaces/{SPACE_KEY}/pages/{PAGE_ID}
```

Or use the `webUrl` field from the response if available. Always provide this URL to the user.

---

### Phase 6: Verification & Delivery

After publishing:

1. **Verify the page was created** by fetching it back:
   ```
   getConfluencePage: pageId = [newly created page ID]
   ```

2. **Check content integrity:**
   - All sections present
   - Table formatting renders correctly
   - No broken markdown
   - Total word count within target range (Rule 1: 400-550 simple, 550-800 medium, 1500-2000 complex)

3. **Final confidence summary:** Display the final confidence scores for all sections

4. **Flag gaps:** Note sections that still have `[To be confirmed]` markers

5. **Provide the Confluence page URL** to the user

6. **⚠️ MANDATORY: Diagram upload instruction:**
   > "Please upload the architecture diagram to the Confluence page: edit the page → drag the PNG into the Architecture section → save."
   >
   > [View architecture diagram](computer:///path/to/arch_diagram.png)

---

## Content Quality Standards

### Design Plan Structure: Section Details

Each section has specific content expectations based on analysis of real One Thousand design plans:

#### Opening Section — Deterministic (Rule 2 decides style)
**Style A — OT Template (Yellow Bikes, Blue Homes UC2 pattern):** Template formula (see Rule 3) — 2 paragraphs, ~60-80 words. No heading.

**Content density for Style A:**
- Paragraph 1: Client name, use case, timeline (N weeks), sprint count, core benefit. ~50 words.
- Paragraph 2: 1 sentence, aspirational closing. ~20 words.
- **INCLUDE:** client name, use case noun, week count, sprint count, one key benefit.
- **EXCLUDE:** tech stack details, team names, architecture, requirements, rationale.

**Style B — Project Description (MICUBO pattern):** `## Overview` heading, 2-3 paragraphs (~150 words). Content from hackathon doc / user input only.

**Content density for Style B:**
- Paragraph 1: What the product IS and what it does. ~50 words.
- Paragraph 2: Technology approach (LLMs, TTS, cloud platform) and delivery model. ~50 words.
- Paragraph 3 (if needed): External collaborations — bullet list with partner name + role. ~50 words.
- **INCLUDE:** product description, tech approach at category level (LLM, TTS — not model names), cloud platform, external partners + their role.
- **EXCLUDE:** internal team names, detailed architecture, sprint details, requirements list, cost/effort data.

**Style C — No opening (Colorful-Toys pattern):** Jump straight to Key Requirements or Architecture. Zero words.

#### Key Requirements Section — IF no scope doc exists AND requirements in source

**Content density rules (measured from originals):**
- **Max 6 bullets** (Colorful-Toys: 6, Blue Homes UC2: 6)
- **7-15 words per bullet** (Blue Homes UC2 avg: 7.2 words, Colorful-Toys avg: 12.3 words)
- **Grammar:** Start with imperative verb or noun phrase → "Develop an AI-based...", "Support at least 10...", "AI-powered voicebot for..."
- **Total section: ~70-80 words max**

**What GOES IN each bullet (pick ONE per bullet):**
- A major deliverable/capability ("Develop an AI-based product advisor")
- A quantified scope constraint ("Support at least 10 reference room types")
- An integration requirement ("Ensure integration with HABA's data systems (PXM, SAP)")
- A non-functional constraint ("Handle 200 parallel calls", "Hosted on Microsoft Azure")
- A collaboration requirement ("Collaboratively define UX positioning with [client]")

**What gets FILTERED OUT — even if it's in the source:**
- ❌ Rationale or justification for why a requirement exists
- ❌ Implementation details (algorithms, frameworks, specific APIs)
- ❌ Stakeholder names (use system/team names instead)
- ❌ Success criteria or KPIs ("must achieve 95% accuracy")
- ❌ Contingency plans or fallback approaches
- ❌ Use case framing ("UC1:", "UC2:") — write as flat list
- ❌ More than 6 bullets — if source has 15 requirements, pick the 6 most impactful

#### Notes & Dependencies Section — IF 1-3 dependencies NOT in Key Reqs or epics

**Content density rules (measured from Colorful-Toys — only 2025+ design with this section):**
- **Max 2 bullets** (never 3+)
- **11-17 words per bullet** (avg: 14 words)
- **Format:** `**Label:** [concrete items/actions]`
- **Total section: ~30 words max**

**What GOES IN each bullet:**
- External team deliverables the client must provide ("PXM & SAP data access, 10+ reference rooms, Azure access")
- Process cadence ("Weekly joint check-ins with IT & UX teams")

**What gets FILTERED OUT:**
- ❌ Internal OT task dependencies (those go in Timeline epics)
- ❌ Assumptions or risks
- ❌ Resource allocation or staffing
- ❌ Anything already captured in Key Requirements bullets or Timeline epic text

#### Architecture Section — ALWAYS INCLUDE

**Content density rules:**
- **Image only by default = 0 words of prose** (3/4 designs: just the image)
- Diagram placeholder: `**[Architecture diagram to be added — PNG file provided separately]**`
- **1-sentence intro (max 25 words):** ONLY IF source explicitly says architecture "needs to be refined" or is "initial/high-level." Reference: Blue Homes UC2 = "The following diagram is an initial, high level and indicative of an architecture that still needs to be refined."
- Add `## Updated Architecture` with second diagram ONLY IF source shows architecture evolved (1/4 designs: MICUBO).

**What gets FILTERED OUT:**
- ❌ Text descriptions of architecture components (NEVER)
- ❌ Data flow explanations
- ❌ Technology justifications
- ❌ Component lists
- ❌ Anything that describes what the diagram shows — let the diagram speak

#### Sprint Plan Overview — IF 7+ sprints

**Content density rules (measured from MICUBO):**
- **One line per sprint:** "**Sprint N (CW XX/YY):** [5-15 word description]"
- **8-15 words per line** (avg: ~12 words)
- **Total: ~100-150 words** for 9 sprints
- Can show "Original plan" + "Updated plan" if plan evolved — but each version follows same density

**What GOES IN each line:**
- Sprint number + calendar weeks + one-phrase goal
- Reference: "Sprint 1 (KW 32/33): Data layer setup: Stories DB, Audio Storage + start stories gen"

**What gets FILTERED OUT:**
- ❌ Epic-level detail (that's in the Timeline table)
- ❌ Category prefixes (just describe the goal)
- ❌ Effort estimates
- ❌ Dependencies or notes

#### Timeline & Design Table Section (CORE DELIVERABLE) — ALWAYS INCLUDE

**This is the most important section.** All content density numbers below are measured from the 4 originals.

**GOAL column density:**
- **10-20 words per goal** — one sentence describing the sprint's primary objective
- **Grammar:** Noun phrase or imperative → "Data Layer + Infrastructure Setup", "E2E Prototype", "Handle Technibike data"
- **INCLUDE:** What this sprint achieves at a high level
- **EXCLUDE:** How it achieves it (that's in Epics), effort data, dependencies

**Sprint names and goals:** When a scope document provides explicit sprint names or goals, use them verbatim in the Goal column — do not paraphrase or generalize.

**Sprint durations in the Sprint column:** When the scope doc specifies non-standard durations (e.g., "1-week sprint", "refinement sprint"), reflect this in the Sprint column label, e.g. `Sprint 4 (1 week)`.

**EPICS column density (THE critical content filter):**

| Complexity | Words/sprint | Categories/sprint | Words/category item |
|------------|-------------|-------------------|-------------------|
| Simple (≤3 sprints) | 30-45 words | 4-6 | 5-12 words |
| Medium (4-6 sprints) | 50-85 words | 4-6 | 8-18 words |
| Complex (7+ sprints) | 80-150 words | 4-8 | 10-25 words |

**Epic item grammar:** `**Category:** [action phrase]; [action phrase].`
- Use semicolons to separate multiple items within one category
- Use `+` for 1-2 sub-items that extend the category's scope
- Each action phrase: verb + object + qualifier → "Connect to Webshop/SAP data sources", "Implement basic recommendation prototype"

**Standard category order (use only categories relevant to the sprint):**
1. **Scope:** (alignment, requirements definition — Sprint 1 only)
2. **Data:** (ingestion, synchronization, transformation, validation)
3. **AI:** / **Modelling:** (algorithms, models, rules, optimization)
4. **Integration:** (APIs, systems, connections, UI, deployment)
5. **Testing:** (validation, UAT, load/performance)
6. **Documentation:** (guides, handover, training)

**What GOES IN epic items:**
- ✅ Feature-level planned tasks ("Implement basic recommendation prototype")
- ✅ Specific system names from source ("Connect to PXM/SAP", "Setup Azure Speech-to-Text")
- ✅ Client domain terms exactly as stated ("Produktberater", "Baugruppen", "Mietervertragsnummer")
- ✅ Quantified scope from source ("at least 10 room types", "200 parallel calls")

**What gets FILTERED OUT from epic items — even if it's in the hackathon doc:**
- ❌ Implementation-level tasks ("Refactor login handler", "Fix bug #423", "Review PR")
- ❌ Algorithm names/choices UNLESS that IS the feature ("SARIMA model" → NO; "recommendation rules" → YES)
- ❌ Specific file names or dataset names ("EWG_Cockpit/CAB_Abwesenheiten.xlsx")
- ❌ PoC results or accuracy metrics ("achieved ~80% accuracy")
- ❌ Conditional logic ("only in case the IT team is not able to...")
- ❌ Parenthetical rationale ("(because the API doesn't support...)")
- ❌ Status markers ("[DONE]", "[WIP]", "→ Done")
- ❌ Individual person names (use roles: "IT team", "application team")
- ❌ Effort estimates within epics (goes in 5th column if discussed)
- ❌ Success criteria ("must achieve 95% accuracy", "response time < 200ms")
- ❌ Risk mitigation steps
- ❌ Meeting schedules or process details
- ❌ Sub-tasks beyond 1 level of "+" nesting
- ❌ Anything learned DURING sprints (temporal contamination — Rule 7)

**CLIENT EFFORT column density (5th column, IF discussed):**
- **20-30 words per cell**
- **Format:** `[N] PD: ([Team]) [action1] + ([Team2]) [action2]`
- **Unit:** Person-days (PD) only — never hours, FTEs, or percentages
- **Actions:** Concrete deliverables only ("Validate web interface", "Provide data exports", "Run integration tests")
- **EXCLUDE:** Success criteria, contingencies, meeting time, rationale

**Release event row:** ONLY IF source explicitly mentions a release milestone. Format: `| Release event | CW XX | | Yay 🎉 🥂 🎈 |`

**All sprints start at Sprint 1 — NEVER Sprint 0.**

**Sprint sequencing must follow logical dependency chain (see Rule 8).**

#### Design Decisions Section — IF 1-3 explicit tech decisions in source

**Content density rules (measured from MICUBO — only 2025+ design with this):**
- **Max 2 items** (MICUBO has 2)
- **15-30 words per item** — state the decision + brief context
- Can include a supporting diagram/image
- Reference: "Send the board configuration with each story request" / "Store id to asset name mapping in the relational database"

**What GOES IN:**
- The decision itself (what was chosen)
- Brief technical context (what the alternatives were or why this matters)

**What gets FILTERED OUT:**
- ❌ Full evaluation of alternatives
- ❌ Performance benchmarks
- ❌ Implementation details of how to execute the decision

#### ~~Effort Estimation Section~~ — NEVER INCLUDE
- Eliminated in all 2025+ designs (0/4 have it)
- If client effort was discussed → put in timeline table's 5th column (Rule 5)
- If client effort was NOT discussed → use 4-column table, no effort anywhere

### Tone & Voice
- Professional, partnership-focused, results-oriented
- First person plural ("we") when describing joint work
- Confident but not arrogant
- Technical precision without jargon overload
- Use client's exact domain terminology

### Evidence-Based Writing
- Every claim traces to scope document, hackathon document, or customer conversation notes
- Use exact terminology from source material
- Never invent metrics, KPIs, or performance numbers
- Never add features or sprints not discussed in source
- Never assume timelines unless explicitly discussed
- **Temporal rule:** Sprint designs capture PLANNED work. Never include results, findings, status updates, or implementation details that would only be known after sprints begin. Confluence project pages contain post-hoc data — do not copy content from them.

---

## Anti-Hallucination Rules (Critical)

Read the full rules at `references/anti-hallucination-rules.md`. Key rules for design plans:

1. **Sprint durations:** Use durations from the scope document. If no scope doc exists, only use durations explicitly discussed in other sources. Do NOT default to "2-week sprints" — many projects have mixed 1-week and 2-week sprints as defined in the scope doc.
2. **Calendar weeks:** ONLY use specific CW numbers if provided. Otherwise use relative timing.
3. **Effort estimates:** ONLY include if mentioned in source. Don't invent person-day estimates.
4. **Architecture components:** ONLY include components mentioned in hackathon or scope doc.
5. **Technology choices:** Use exact technology names from source (e.g., "Firestore" not "NoSQL database").
6. **Feature names:** Preserve exact terminology — don't rename or rebrand features.
7. **Status markers:** Do NOT include [DONE] or [WIP] markers — sprint designs are created before work begins. These markers are added later during project execution.
8. **Client names and roles:** Use exact names from source. Don't invent stakeholder roles.
9. **Dependencies:** Only list dependencies mentioned in source.
10. **Timeline conflicts:** If hackathon and customer say different things, flag BOTH — don't pick one.

**Decision tree for uncertain content:**
```
I want to include [claim/timeline/component] because [reason]

Is it in the scope document?
├─ YES → Include (scope doc is authoritative)
└─ NO  → Is it in the hackathon doc or customer conversation notes?
    ├─ YES → Include
    └─ NO  → Is it metadata from Close CRM (dates, deal value, client name)?
        ├─ YES → Include as metadata (weave into intro or timeline dates)
        └─ NO  → Is it from Confluence pages created during the project?
            ├─ YES → DO NOT INCLUDE (temporal contamination — this data didn't exist at planning time)
            └─ NO  → Does the client need to decide?
                ├─ YES → Include as [To be confirmed]
                └─ NO  → DO NOT INCLUDE
```

---

## File Paths (Relative to Skill Directory)

```
sprint-design/
├── assets/                                # Shared assets
├── scripts/
│   └── generate_architecture_diagram.py   # Graphviz diagram generator (same as scope skill)
├── references/
│   ├── anti-hallucination-rules.md        # Anti-hallucination rules
│   └── design-plan-structure.md           # Structure templates based on real examples
└── SKILL.md                               # This file
```

**Shared with scope-document-generator:**
- `generate_architecture_diagram.py` — Same script, same JSON format, same rendering pipeline
- `anti-hallucination-rules.md` — Same rules apply to design plans

---

## Examples: Design Plans by Complexity

These examples show the ideal output at different scales. Adapt section inclusion based on Rule 2.

### Example A: Simple Project (~500 words, 3 sprints — Colorful-Toys pattern)

```markdown
### Key Requirements

- Develop an AI-based product advisor that provides accurate recommendations based on user requirements.
- Support at least 10 reference categories, extendable in the future.
- Build the foundational chat interface and API endpoints for website integration.
- Ensure integration with client data systems and cloud environment.

### Notes & Dependencies

- **Client deliverables:** Data access, reference categories, cloud environment access.
- **Important collaboration:** Weekly joint check-ins with IT & UX teams.

### Architecture

[Architecture diagram to be added — PNG file provided separately]

### Timeline & Sprints

| **Sprint / Phase (2 weeks)** | **Timeline** | **Goal** | **Epics (High-Level Features)** |
| --- | --- | --- | --- |
| **Sprint 1: Foundation & First Prototype** | CW X–Y | Establish data foundation, set up environment, deliver first prototype. | **Data:** Connect to data sources; ingest reference data and product catalog. **AI:** Implement basic recommendation prototype. **Integration:** Develop chat API skeleton and simple UI mockup. **Testing:** Validate data ingestion and sample recommendations. |
| **Sprint 2: Enhanced Recommendation** | CW X–Y | Implement recommendation rules and enhance the system. | **AI:** Develop recommendation rules (influence parameters, mappings). **Integration:** Implement web integration approach; connect chat API. **Testing:** Conduct internal user tests; refine responses based on feedback. |
| **Sprint 3: Integration & Production Readiness** | CW X–Y | Finalize website integration, optimize UX, prepare for production. | **Data:** Final data synchronization and validation. **AI:** Optimize recommendation precision; improve explainability. **Integration:** Joint testing with web developers; finalize chat assistant integration. **Testing:** End-to-end UAT; load/performance checks. **Documentation:** Technical handover and operational guide. |
```

Note: This pattern uses `###` headings, 4-column table, no OT intro, no client effort column, no release event row. Matches actual Colorful-Toys output.

### Example B: Medium Project (~700 words, 4-5 sprints — Yellow Bikes / Blue Homes UC2 pattern)

Same structure as Example A but with:
- OT intro template (Style A) at the top
- More sprint rows (4-5)
- 5-column table IF client effort was discussed (otherwise 4-column)
- Key Requirements section IF no scope doc exists

See Yellow Bikes (page 868515919) or Blue Homes UC2 (page 821428302) for real examples.

### Example C: Complex Project (~2000 words, 7+ sprints — MICUBO pattern)

Same core structure plus sections triggered by complexity:
- **`## Overview`** (Style B) — product needs explaining → triggered
- **`## Sprint Plan Overview`** — 7+ sprints → triggered
- **`## Design Decisions`** — explicit tech decisions in source → triggered
- **NO separate Effort Estimation** — even at this complexity level

See MICUBO (page 1085309264) for a real example.

**Key principle:** Section inclusion is determined by Rule 2's IF/THEN conditions, not by "complexity feel." The Timeline & Design table is ALWAYS the core deliverable — other sections support it.

---

## Reference Examples in Confluence (2025+ Only)

This skill's structure is derived from analysis of these **2025+ OT design plan pages** only. Pre-2025 designs (Blue Homes original Dec'24, SWen, etc.) are excluded — they use outdated patterns (Sprint 0, separate Effort Estimation).

1. **Yellow Bikes** (Jan 2025) — **Reference for concise medium projects with client effort**
   - Page ID: `868515919`
   - **Sections used:** OT intro (Style A), Architecture image, 5-column Timeline table (with "Efforts from the client" column). ~550 words.
   - **Why 5 columns:** Client effort was explicitly discussed → triggered 5th column.
   - **Why no Key Requirements:** Context was clear from intro.

2. **Blue Homes UC2** (Mar 2025) — **Reference for medium projects with Key Requirements**
   - Page ID: `821428302`
   - **Sections used:** OT intro (Style A, incomplete), Key Requirements (6 bullets), Architecture image + intro sentence, 5-column Timeline table (with "Review" column), Release event row. ~700 words.
   - **Why Key Requirements:** No separate scope doc existed.
   - **Why Release event:** Source explicitly mentioned go-live milestone.

3. **Colorful-Toys Produktberater** (Oct 2025) — **Reference for CONCISENESS (simple projects)**
   - Page ID: `1444479015`
   - **Sections used:** Key Requirements (6 bullets), Notes & Dependencies (2 bullets), Architecture image, 4-column Timeline table. ~450 words.
   - **Why Key Requirements:** No scope doc existed.
   - **Why Notes & Dependencies:** 2 critical external dependencies not in Key Reqs or timeline.
   - **Why no opening:** Simple project, context clear → Style C.

4. **MICUBO** (Dec 2025) — **Reference for complex multi-sprint projects**
   - Page ID: `1085309264`
   - **Sections used:** Overview (Style B, custom), Initial + Updated Architecture, Sprint Plan Overview, 4-column Timeline table, Design Decisions (2 items). ~2000 words.
   - **Why Style B:** Product was novel (AI storytelling game), needed explaining.
   - **Why Sprint Plan Overview:** 9 sprints → triggered by 7+ rule.
   - **Why Design Decisions:** 2 explicit tech decisions in source.

**Word count targets by complexity:**

| Complexity | Sprint count | Target words | Reference |
|------------|-------------|-------------|-----------|
| Simple | 2-3 sprints | 400-550 | Colorful-Toys (~450) |
| Medium | 4-6 sprints | 550-800 | Yellow Bikes (~550), Blue Homes UC2 (~700) |
| Complex | 7+ sprints | 1500-2000 | MICUBO (~2000) |

---

## Language Support

### English (Default)
All section headings, templates, and examples in this skill are in English.

### German
When generating German design plans:
- Use German section headings: "Überblick", "Kernanforderungen", "Architektur", "Sprint-Übersicht", "Zeitplan & Design", "Designentscheidungen", "Aufwandsschätzung"
- Use `[Noch zu bestätigen]` instead of `[To be confirmed]`
- Preserve client's domain terminology in original language (do NOT translate domain terms)
- For mixed teams, section headings can remain in English while content is in German — ask user preference
- Anti-hallucination markers: see `references/anti-hallucination-rules.md` language section
