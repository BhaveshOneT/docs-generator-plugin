---
name: handover-document
description: >
  Generate professional One Thousand client handover documents as Confluence pages.
  Triggers on: "handover document", "handover doc", "project handover",
  "client handover", "create handover", "generate handover", "handover for this",
  "solution handover", "technical handover", "handover documentation",
  "übergabe dokument", "übergabedokument", "projekt übergabe".
  Transforms project artifacts (scope documents, debrief documents, architecture
  diagrams, code repositories, deployment configs, and sprint histories) into
  professional handover Confluence pages with confidence-scored content generation,
  iterative gap-filling, and anti-hallucination verification.
  Supports English and German. Primary output is a Confluence page placed as a
  direct child of the project space root page. Optional secondary output: branded
  DOCX with green cover page.
license: Proprietary
---

# Handover Document Generator Skill

## Overview

This skill generates **professional One Thousand client handover documents as Confluence pages** from project source material. It takes uploaded documents (scope docs, debrief docs, architecture diagrams, READMEs, sprint notes, deployment configs) and produces a publication-ready handover Confluence page that combines solution documentation and architecture documentation into a single comprehensive deliverable.

The workflow: Collect inputs (user uploads documents) → Extract information with gap detection → Generate content with confidence scoring → Iteratively request missing documents/info → Run anti-hallucination verification → Create Confluence page in the project space → Deliver.

**Primary Output:** A Confluence page titled "Handover Dokument" (or "Handover Document" in English), placed as a **direct child of the project space root page** — following the flat single-page structure used by existing handover documents (no sub-pages).

**Optional Secondary Output:** A branded DOCX file with green cover page (#19A960), One Thousand logo, and professional typography. Only generated if the user explicitly requests a DOCX in addition to the Confluence page.

---

## When to Use This Skill

**ALWAYS invoke this skill when the user's request matches ANY of these patterns:**

- User says "handover document", "handover doc", or "project handover"
- User says "create/generate/write a handover" for some project
- User says "client handover", "solution handover", or "technical handover"
- User has project artifacts and wants a "handover deliverable" or "handover page"
- User says "übergabe dokument" or "übergabedokument" (German)
- User is preparing a formal project handover for a client
- User needs to document a solution for client self-management

**Do NOT invoke for:** hackathon debriefs (use hackathon-debrief), scope documents (use scope-document-generator), slide decks (use hackathon-presentation), internal employee handovers without a client deliverable.

---

## Inputs

The **primary inputs** for a handover document are:

1. **GitHub Repository** — The project's code repository. This is the richest source for: dependencies & libraries (requirements.txt, package.json, Pipfile), deployment instructions (README, Dockerfile, Terraform, CI/CD configs), architecture (code structure, service definitions, API routes), code package details, and known limitations (TODOs, open issues).

2. **Confluence Documentation** — The project's Confluence space containing: scope documents, debrief documents, sprint design plans, architecture diagrams, meeting notes, and any other project documentation pages.

### How Input Collection Works

1. **Ask the user for the GitHub repo URL and Confluence space** (see Phase 1).

2. **Clone the GitHub repo** and extract technical information:
   - README.md / README files → project overview, setup instructions, deployment steps
   - requirements.txt / package.json / Pipfile → dependencies & libraries
   - Dockerfile / docker-compose.yml → deployment & infrastructure
   - Terraform / IaC files → cloud infrastructure setup
   - .env.example / config files → environment configuration, credentials structure
   - CI/CD configs (.github/workflows, Jenkinsfile) → deployment pipeline
   - Source code structure → architecture, features, API endpoints
   - CHANGELOG / git history → development history
   - Open issues / TODOs in code → known limitations

3. **Fetch Confluence pages** from the project space:
   - Use `searchConfluenceUsingCql` or `getPagesInConfluenceSpace` to find all relevant pages
   - Read key pages: scope document, debrief document, sprint design plan, architecture pages
   - Extract: project overview, timeline, features, IP/legal, data sources, development history, recommendations

4. **Merge and cross-reference** information from both sources. GitHub is authoritative for technical details (dependencies, deployment, code). Confluence is authoritative for project context (timeline, decisions, client info, IP/legal).

5. **Score each section's confidence** based on what was extracted.

6. **For sections below threshold**, ask the user to provide additional information or upload supplementary documents.

7. **Repeat until all sections pass** or the user says to proceed anyway.

### Supplementary Inputs (Optional)

If the GitHub repo + Confluence don't cover everything, the user can also provide:
- Architecture diagrams (PNG, PDF) — uploaded directly
- Credential/access documents — text input (never stored in files)
- Additional context — verbal answers to gap-filling questions

### Language Selection

Ask the user: **English or German?**

This determines section titles, content language, and placeholder markers.

---

## Workflow

### Phase 1: Input Collection

Ask the user using AskUserQuestion:

1. **GitHub Repository URL:** The project's GitHub repo (e.g., `https://github.com/org/project-name`). This is the primary technical source.
2. **Confluence Space:** Which Confluence space contains the project documentation? (Space key or name. If unknown, the skill will search by project/client name.)
3. **Language:** English or German?
4. **Client Name:** Who is the handover for? (if not extractable from repo/Confluence)
5. **Also generate DOCX?** Does the user want a branded DOCX file in addition to the Confluence page? (Default: No, Confluence only)

**After collecting inputs:**

1. **Clone the GitHub repo** to a temporary directory:
   ```bash
   git clone <repo_url> /tmp/handover_repo
   ```
   If the repo requires authentication, ask the user for a PAT or use an existing GitHub CLI session.

2. **Scan the repo** for key files:
   ```bash
   # Find documentation and config files
   find /tmp/handover_repo -maxdepth 3 \( \
     -name "README*" -o -name "requirements*.txt" -o -name "package.json" -o \
     -name "Pipfile" -o -name "Dockerfile" -o -name "docker-compose*" -o \
     -name "*.tf" -o -name ".env.example" -o -name "CHANGELOG*" -o \
     -name "Makefile" -o -name "*.yml" -o -name "*.yaml" \
   \) -type f
   ```
   Read each discovered file to extract relevant information.

3. **Fetch Confluence pages** from the project space:
   - Use `getPagesInConfluenceSpace` to list all pages
   - Read the key pages (scope doc, debrief, sprint design, architecture) using `getConfluencePage` with `contentFormat: "markdown"`
   - Extract project context, timeline, decisions, client info

**Note:** If the user also wants a DOCX, Python dependencies (`python-docx`, `Pillow`) are installed automatically by the plugin's SessionStart hook. No manual `pip install` is needed.

---

### Phase 2: Content Extraction

#### Parallel Reference File Loading

Before generating, Claude **MUST** read these reference files. **Read ALL THREE files in parallel** (use multiple Read tool calls in a single message):

- `references/section-templates-en.md` OR `references/section-templates-de.md` — prompt templates for the chosen language
- `references/anti-hallucination-rules.md` — verification framework
- `references/sample-excerpts-de.md` OR `references/sample-excerpts-en.md` — tone/structure examples

**Important:** These are data-loading calls, not generation steps. Reading them in parallel produces the exact same context as reading them sequentially.

#### Extract from Source Material

From the **GitHub repo** and **Confluence pages**, extract information for each of the 13 sections below. Build a structured data object mapping each section to its extracted content.

**Source priority per section** (GitHub = GH, Confluence = CF):

| Section | Primary Source | What to Extract From |
|---------|---------------|---------------------|
| Project Overview | CF (scope doc, debrief) | Project purpose, client, scope, team contacts |
| Project Timeline | CF (sprint design, debrief) | Sprint breakdown, dates, deliverables |
| Features & Workflows | GH (code, README) + CF | API routes, services, features from code + docs |
| IP & Legal | CF (scope doc) | IP clauses, license info, GDPR |
| Data Sources | CF (debrief, scope) + GH | Data descriptions from docs + data configs in code |
| Development History | CF (debrief, sprint notes) | Per-sprint narrative, decisions, metrics |
| Architecture | GH (code structure, configs) + CF | Service layout, infra configs, architecture docs |
| Dependencies & Libraries | GH (requirements.txt, package.json, Dockerfile) | **Exact versions from repo — authoritative** |
| Deployment Instructions | GH (README, Dockerfile, Terraform, CI/CD) | **Exact commands from repo — authoritative** |
| Known Limitations | GH (issues, TODOs) + CF | Open issues, TODOs in code, deferred items in docs |
| Code Package | GH (repo structure) | Repo URL, contents, .env handling, test status |
| Credentials & Access | CF + user input | 1Password links, portal URLs, access grants |
| Recommendations | CF (debrief, scope) | Next steps, improvement suggestions |

**Extraction targets per section:**

1. **Project Overview:** Project name, client name, project purpose, scope delivered, target users, key features, quality systems (if any), team contacts (OT side + client side). *Source: Confluence scope doc + debrief.*

2. **Project Timeline:** Sprint breakdown with dates (calendar week notation preferred), high-level deliverables per sprint, overall project duration. *Source: Confluence sprint design plan + debrief.*

3. **Features & Workflows:** All major functionalities, critical end-to-end workflows, user-facing capabilities, API endpoints (if applicable). *Source: GitHub code (API routes, service files) + Confluence feature descriptions.*

4. **IP & Legal Considerations:** IP ownership status (who owns the code, data, model outputs), license compliance (open-source licenses used, any restrictions), non-compete / preferred partner clauses, data protection compliance (GDPR, anonymization), client sign-off status. *Source: Confluence scope doc + contracts.*

5. **Data Sources:** All data sources used (name, type, format, volume, quality observations), data access methods, storage locations. *Source: Confluence debrief + GitHub data configs.*

6. **Development History:** Per-sprint narrative — what was built, key decisions made (with rationale), technical challenges encountered, metrics improvements (before/after per sprint), deferred items and why. *Source: Confluence debrief + sprint notes.*

7. **Architecture:** Architecture diagram (extract or generate), numbered workflow description (step-by-step data/request flow), component table (Name | Type | Description), connection table (Source | Target | Method | Auth | Protocol) if available. *Source: GitHub code structure + Terraform/Docker configs + Confluence architecture pages.*

8. **Dependencies & Libraries:** Main dependencies (OS, language, runtime versions), OS-level packages, language-specific packages with version pinning, third-party APIs. *Source: GitHub — requirements.txt, package.json, Pipfile, Dockerfile. This section must be extracted directly from the repo, not synthesized.*

9. **Deployment Instructions:** Cloud infrastructure setup (Terraform/IaC if applicable), code deployment method (step-by-step with commands), environment configuration, monitoring setup. *Source: GitHub — README deploy section, Dockerfile, Terraform files, CI/CD configs, Makefile.*

10. **Known Limitations & Open Issues:** Current limitations of the solution, known bugs or edge cases, features discussed but not implemented, technical debt. *Source: GitHub issues + TODO comments in code + Confluence debrief deferred items.*

11. **Code Package:** Repository URL or zip file delivery method, what's included vs excluded, env file handling, code quality status (linting, tests). *Source: GitHub — repo URL, directory structure, .env.example, test configs.*

12. **Credentials & Access:** All access credentials organized by system (1Password links preferred), portal URLs, who has access, expiry dates, how to rotate/renew. *Source: Confluence + user input. Never extract actual secrets from code.*

13. **Recommendations & Next Steps:** Short-term improvements, medium-term extensions, long-term vision, maintenance plan, support arrangement. *Source: Confluence debrief + scope doc recommendations.*

---

### Phase 3: Section Generation with Confidence Scoring

Generate each section using the prompt templates from the reference files.

#### Confidence Scoring System

After generating each section, self-assess a **confidence score (0-100)** based on five dimensions (each 0-20 points):

1. **Source Grounding (0-20):** Is every claim traceable to the source document?
2. **Specificity (0-20):** Are names, tools, versions, URLs specific rather than generic?
3. **Completeness (0-20):** Does the section cover its full purpose per the template?
4. **Actionability (0-20):** Can someone act on this content? (deploy, access, troubleshoot)
5. **Anti-Hallucination (0-20):** Is the section free of invented details?

#### Section-Specific Thresholds

| Section | Threshold | Rationale |
|---------|-----------|-----------|
| Project Overview | 80 | Core identification — must be precise |
| Project Timeline | 75 | Structural, some synthesis allowed |
| Features & Workflows | 80 | Core deliverable description — must be accurate |
| IP & Legal | 85 | Legal accuracy critical — affects contracts |
| Data Sources | 80 | Technical accuracy critical |
| Development History | 70 | Narrative allows synthesis from sprint notes |
| Architecture | 75 | Diagram + description, some generic framing OK |
| Dependencies & Libraries | 90 | Pure data extraction — must be exact |
| Deployment Instructions | 85 | Must be actionable step-by-step |
| Known Limitations | 75 | Some synthesis from source allowed |
| Code Package | 85 | Access info must be accurate |
| Credentials & Access | 90 | Security-critical, must be exact |
| Recommendations & Next Steps | 70 | Forward-looking, allows synthesis |

#### Iterative Review Loop

After scoring all sections, if ANY section falls below its threshold:

1. **Show the user a summary table:**
   ```
   Section                        Score   Status
   ──────────────────────────────────────────────
    1. Project Overview              85     ✓ Pass
    2. Project Timeline              72     ✗ Needs input (below 75)
    3. Features & Workflows          88     ✓ Pass
    4. Data Sources                  65     ✗ Needs input
    5. Development History           74     ✓ Pass
    6. Architecture                  80     ✓ Pass
    7. Dependencies & Libraries      42     ✗ Needs input
    8. Deployment Instructions       38     ✗ Needs input
    9. Known Limitations             70     ✗ Needs input (below 75)
   10. Code Package                  55     ✗ Needs input
   11. Credentials & Access          30     ✗ Needs input
   12. Recommendations               72     ✓ Pass
   ```

2. **For each failing section, ask the user to upload specific documents or provide text.** Be precise about what's missing:
   - "Dependencies scored 42/100. I found no requirements.txt, package.json, or dependency list in the uploaded documents. Can you upload or paste the project's dependency file?"
   - "Deployment Instructions scored 38/100. The source documents don't describe how to deploy the solution. Can you upload a deployment guide, README with deploy steps, or describe the deployment process?"
   - "Credentials scored 30/100. No credential information was found. Can you provide: (a) 1Password vault links, (b) API key locations, (c) portal URLs with access instructions?"

3. **When the user provides additional documents or text**, re-extract, re-generate the failing sections, and re-score.

4. **Repeat until all sections pass** OR the user explicitly says to proceed anyway ("proceed anyway", "good enough", "skip this").

**The user can always override** — in which case, proceed with `[To be confirmed]` / `[Noch zu bestätigen]` markers on weak sections.

---

### Phase 4: Anti-Hallucination Verification

Run the 4-check verification framework from `references/anti-hallucination-rules.md`:

1. **Metrics Check (20%):** Every number, version, URL, date traces to source
2. **Terminology Check (20%):** System names, service names, tool names match source exactly
3. **Completeness Check (30%):** All components from source appear, no sections empty
4. **Actionability Check (30%):** Deployment steps are executable, credentials are locatable, code is accessible

Flag any section that fails. Ask the user for corrections.

---

### Phase 5: Document Assembly — Confluence Page

The primary output is a **Confluence page**. Optionally, a DOCX file can also be generated.

#### Step 5.1: Determine Confluence Space & Parent Page

The handover page must be placed correctly in the Confluence hierarchy. Existing handover documents follow a **flat single-page** structure: each handover is a direct child of the project space's root page (no sub-pages).

**Discovery workflow:**

1. **If the user provided a Confluence space key/name** in Phase 1, use it directly.

2. **If not**, search for the project space:
   ```
   searchConfluenceUsingCql(
     cloudId: "<cloud_id>",
     cql: "type = \"space\" AND space.title ~ \"<project_or_client_name>\""
   )
   ```

3. **Find the root page** of the target space:
   ```
   getPagesInConfluenceSpace(
     cloudId: "<cloud_id>",
     spaceId: "<space_id>",
     limit: 1
   )
   ```
   Then use `getConfluencePageDescendants` to verify the root page ID and see existing children.

4. **Verify no duplicate handover page exists** under the root. If one does, ask the user whether to:
   - Update the existing page (use `updateConfluencePage`)
   - Create a new page alongside it (append date or version suffix to title)

5. **Set the parent page** to the space root page ID.

**Confluence Cloud ID:** Use `getAccessibleAtlassianResources` to get the cloud ID if not already known from the session context. For One Thousand's Confluence, the cloud ID is `e59f9c4b-2664-43dd-8c9f-0ed7844ca1c3`.

#### Step 5.2: Build Markdown Content

Assemble the full page content as a **single markdown string**. The Confluence `createConfluencePage` API accepts `contentFormat: "markdown"`.

**Page structure:**

```markdown
# Handover Dokument — <Project Name>

**Client:** <Client Name>
**Handover Date:** <Date>
**One Thousand Team:** <Name (Role)>, <Name (Role)>
**Client Team:** <Name (Role)>, <Name (Role)>

---

## 1. Projektübersicht und Hintergrund

<section content as markdown>

---

## 2. Projektzeitplan

<section content as markdown>

...

## 13. Empfehlungen und nächste Schritte

<section content as markdown>
```

**Markdown formatting guidelines for Confluence:**

- Use `#` for H1 (page title — only one), `##` for section headings, `###` for subsections, `####` for sub-subsections
- Use `**bold**` and `*italic*` as standard markdown
- Use `- item` for bullet lists, `1. item` for numbered lists
- Use standard markdown tables (`| Col1 | Col2 |` with `|---|---|` separator)
- Use triple-backtick code blocks for commands, config snippets, dependency lists
- Use `---` horizontal rules between major sections
- Architecture diagrams: If available, upload as an attachment separately and reference with `![Architecture Diagram](attachment_url)`. If not possible, describe the architecture in text with the numbered workflow pattern.

**Content JSON (intermediate format):**

The content is still assembled via an intermediate JSON structure for traceability and potential DOCX generation:

```json
{
  "language": "de",
  "project": {
    "name": "Timesheet Analysis",
    "client": "Questax GmbH",
    "handover_date": "Oktober 2025"
  },
  "contacts": {
    "ot_team": [
      { "name": "Linda Eitelberg", "role": "Project Lead" },
      { "name": "Ilya Yalchyk", "role": "Engineer" }
    ],
    "client_team": [
      { "name": "Frank Odenthal", "role": "Technical Lead" }
    ]
  },
  "sections": [
    {
      "id": "project_overview",
      "title": "Projektübersicht und Hintergrund",
      "content": "Markdown content here..."
    },
    ...
  ]
}
```

**Section IDs (in order):** `project_overview`, `project_timeline`, `features_workflows`, `ip_legal`, `data_sources`, `development_history`, `architecture`, `dependencies`, `deployment`, `known_limitations`, `code_package`, `credentials`, `recommendations`

To build the final markdown string from the JSON, concatenate:
1. Page title header (H1) with project name
2. Metadata block (client, date, teams)
3. Horizontal rule
4. Each section: numbered H2 heading + section content (already markdown)
5. Horizontal rules between sections

#### Step 5.3: Create the Confluence Page

Use the `createConfluencePage` MCP tool:

```
createConfluencePage(
  cloudId: "<cloud_id>",
  spaceId: "<space_id>",
  title: "Handover Dokument — <Project Name>",   // or "Handover Document — <Project Name>" for English
  body: "<assembled_markdown_string>",
  contentFormat: "markdown",
  parentId: "<root_page_id>"
)
```

**Title format:**
- German: `Handover Dokument — <Project Name>`
- English: `Handover Document — <Project Name>`
- If updating an existing page, use `updateConfluencePage` with the existing page ID instead.

#### Step 5.4: Deliver

After creating the Confluence page:

1. **Provide the page URL** to the user (construct from: `https://leadmachinelearning.atlassian.net/wiki/spaces/<SPACE_KEY>/pages/<PAGE_ID>/<URL_ENCODED_TITLE>`)
2. **Report the final confidence scores** — show the section-by-section table
3. **Flag any sections** with `[To be confirmed]` / `[Noch zu bestätigen]` markers
4. **Suggest next steps** — e.g., "Review the page in Confluence and fill in the `[Noch zu bestätigen]` items for IP & Legal"

#### Step 5.5: Optional DOCX Generation

**Only if the user explicitly requested a DOCX** in Phase 1:

1. Write the content JSON to `/tmp/handover_content.json`
2. Run the Python DOCX generator:

```bash
SKILL_DIR="<path_to_handover-document_skill>"

python "$SKILL_DIR/scripts/generate_handover_doc.py" \
  --content /tmp/handover_content.json \
  --logo-dir "$SKILL_DIR/assets/logos/" \
  --output /path/to/output/handover_document.docx \
  --arch-diagram /tmp/arch_diagram.png
```

The script generates a branded DOCX with:
- Full-page green (#19A960) title page with logo, display text, project name, client attribution
- Table of contents with dotted leaders and bookmarked links
- Content sections with branded green H1 headings
- Markdown-to-DOCX conversion (headings, lists, tables, code blocks, images, inline formatting)
- Page numbers in bottom-right footer
- A4 page size with 1-inch margins

The `--arch-diagram` flag is optional. If provided, the architecture diagram PNG is embedded in the Architecture section.

---

## Section Structure

### English Document Sections (13 sections)

1. **Project Overview & Background** — Project purpose, scope, key features, team contacts
2. **Project Timeline** — Sprint-by-sprint breakdown with dates and deliverables
3. **Features & Workflows** — Major functionalities, end-to-end workflows, API endpoints
4. **IP & Legal Considerations** — Ownership, licenses, non-compete, data protection, sign-off
5. **Data Sources** — All data sources with formats, volumes, quality, access methods
6. **Development History** — Per-sprint narrative: what was built, decisions, metrics
7. **Architecture** — Diagram + workflow description + component table + connections
8. **Dependencies & Libraries** — OS, runtime, packages with versions, third-party APIs
9. **Deployment Instructions** — Infrastructure setup, code deployment, environment config
10. **Known Limitations & Open Issues** — Current limitations, known bugs, deferred features
11. **Code Package** — Repository/zip delivery, contents, env handling, code quality
12. **Credentials & Access** — All credentials by system, portal URLs, access grants, expiry
13. **Recommendations & Next Steps** — Improvements, extensions, maintenance plan

### German Document Sections (13 sections)

1. **Projektübersicht und Hintergrund**
2. **Projektzeitplan**
3. **Funktionen und Arbeitsabläufe**
4. **Geistiges Eigentum und rechtliche Aspekte**
5. **Beschreibung der verwendeten Datenquellen**
6. **Historie der Projektentwicklung**
7. **Systemarchitektur**
8. **Abhängigkeiten und Bibliotheken**
9. **Anleitung zur Bereitstellung**
10. **Bekannte Einschränkungen und offene Punkte**
11. **Codepaket**
12. **Zugangsdaten**
13. **Empfehlungen und nächste Schritte**

---

## Content Patterns per Section

These patterns are extracted from real One Thousand handover documents and MUST be followed. They define not just the section headings but the **internal content structure** of each section.

### 1. Project Overview & Background

**Pattern:** Opening narrative paragraph → Problem statement → Solution summary → Key capability highlights → Quality/validation system (if applicable)

**Internal structure:**
- Paragraph 1: Client context — who they are, industry, the challenge they face (with scale: e.g., "600 timesheets monthly in varying formats")
- Paragraph 2: Project purpose — what was built, what it does (specific: "API that processes PDF/Word documents, extracts time data, returns structured JSON")
- Paragraph 3: Key capabilities — specific fields extracted, automation gains, output format
- Paragraph 4 (optional): Quality system — traffic light system, confidence scores, validation approach, accuracy metrics

**Anti-pattern:** Do NOT start with generic "One Thousand partnered with..." filler. Start with the client's actual problem.

### 2. Project Timeline

**Pattern:** Sprint-by-sprint table or structured list with calendar week (KW) notation

**Internal structure:**
- Each sprint: Sprint label + date range (KW notation) + one-line objective
- Deliverables per sprint as bullet points
- Final phase: testing/handover phase with dates

**Example format:**
```
Sprint 1 (KW 32 & 33): Infrastructure setup + validation logic
Sprint 2 (KW 34 & 35): Validation refinement + VPN integration
Sprint 3 (KW 36-38): PNG generation + quality assurance
Test & Handover (KW 39-44): Client testing + adjustments + handover
```

### 3. Features & Workflows

**Pattern:** Feature-by-feature description with technical specificity

**Internal structure:**
- One subsection per major feature/capability
- Each feature: what it does + how it works + what value it adds
- Use the client's exact terminology for processes and systems
- Include API schemas/endpoints if the solution exposes an API

### 4. IP & Legal Considerations

**Pattern:** Structured checklist with status indicators

**Internal structure:**
- `### IP Ownership` — Who owns the code, trained models, data outputs. Reference the contract clause. Status of client written confirmation.
- `### License Compliance` — Table of open-source components with license types. Flag any copyleft (GPL) or restrictive licenses. Confirm no violations.
- `### Contractual Clauses` — Key clauses that apply:
  - Non-compete clause (text or reference)
  - Preferred partner clause (text or reference)
  - Code sharing restrictions ("Weitergabe an Dritte" clause)
  - Status: confirmed/pending with date
- `### Data Protection` — GDPR compliance measures taken, anonymization status, data retention policies, DPA (Data Processing Agreement) status

**Anti-pattern:** Do NOT include full legal text. Reference the contract section or provide a one-line summary with "confirmed by [name] on [date]" or "[To be confirmed]".

**Source:** Extract from project contracts, email confirmations, or ask user. This section is often partially or fully `[To be confirmed]` — that is acceptable as long as the structure is present.

### 5. Data Sources

**Pattern:** Structured list with quantitative details

**Internal structure:**
- Per data source: name, type (PDF/CSV/API/DB), volume (count), format variations, quality observations
- How data was provided (anonymized? sample set? production data?)
- Storage location and access method

### 6. Development History

**Pattern:** Per-sprint narrative with decisions and metrics

**Internal structure per sprint:**
- `### Sprint N (dates)` heading
- Sprint objective (one line)
- `#### Details` sub-heading
- What was built/improved (with technical specifics)
- **Decisions made** as bullet points with `**Entscheidung/Decision:**` prefix and rationale
- **Results** with before/after metrics where available (e.g., "validation rate improved from 46% to 79%")
- Items deferred to next sprint and why

**Critical pattern:** Track metric progression across sprints (e.g., accuracy: 14% → 46% → 79% → 90%+ → 92.1%)

### 7. Architecture

**Pattern:** Diagram + numbered workflow + component table

**Internal structure:**
- Architecture diagram (embedded image)
- `### Main Workflow` — numbered steps describing the request/data flow through the system (1. Client sends request → 2. Service processes → 3. Returns response)
- `### Core Components` — table with columns: Name | Type | Description
- `### Connections` (optional) — table with columns: Source | Target | Method | Authentication | Protocol
- `### Private Endpoints` (optional) — table with DNS Name | Private IP | Description (if cloud network architecture is complex)

### 8. Dependencies & Libraries

**Pattern:** Grouped dependency lists with version pinning

**Internal structure:**
- `### Main Dependencies` — OS, language runtime, IaC tool, VCS (with minimum versions)
- `### OS-level Packages` — bullet list of system packages (if applicable)
- `### Language Packages` — code block with exact version pins (requirements.txt or package.json format)
- Third-party API dependencies (if any)

### 9. Deployment Instructions

**Pattern:** Step-by-step with code blocks

**Internal structure:**
- `### Cloud Infrastructure` — IaC approach (Terraform/ARM/etc.), setup steps with commands, state file handling
- `### Code Deployment` — deployment method description, step-by-step with numbered instructions and code blocks
- `### Credential Setup` — where to find deployment credentials, how to authenticate
- Include exact commands (copy-pasteable), URLs, and portal links
- Note any gotchas or expected warnings

### 10. Known Limitations & Open Issues

**Pattern:** Honest, specific list

**Internal structure:**
- Bullet list of current limitations (what the solution cannot do)
- Known edge cases or failure modes
- Features that were discussed/planned but not implemented (with reason)
- Technical debt items

### 11. Code Package

**Pattern:** Delivery details + prerequisites

**Internal structure:**
- How code is delivered (SharePoint link / GitHub repo / zip file)
- Access grants (which email addresses have access)
- What's included vs excluded
- Code quality status (passes linting? has tests?)
- Environment variable handling (.env file, how to obtain)

### 12. Credentials & Access

**Pattern:** System-by-system credential listing

**Internal structure:**
- Per system/service: heading with system name
  - Secure link (1Password share link preferred)
  - Who has access (list of email addresses)
  - Expiry date
  - How to renew/rotate
- Group by: Infrastructure credentials, API credentials, deployment credentials, monitoring access

**CRITICAL:** Never include actual passwords, API keys, or tokens in the document. Only include links to secure credential stores (1Password, Azure Key Vault) and instructions to access them.

### 13. Recommendations & Next Steps

**Pattern:** Time-horizon grouped recommendations

**Internal structure:**
- `### Short-term` — immediate improvements, bug fixes, optimizations
- `### Medium-term` — feature extensions, additional integrations, scaling
- `### Long-term` — strategic vision, platform evolution
- Maintenance plan: who handles ongoing support, SLA if applicable
- Upselling opportunities (for internal OT reference, marked appropriately)

---

## Content Quality Standards

### Tone & Voice
- Professional, technical, precise
- Third person or passive voice for instructions ("The code is deployed by...")
- Active voice for recommendations ("We recommend...")
- No marketing language — this is a technical handover, not a sales document
- Bilingual consistency: if German, ALL content in German (no mixed language except technical terms)

### Formatting Rules
- Code blocks for ALL commands, file paths, URLs, and configuration snippets
- Tables for component listings, connection maps, credential summaries
- Bullet lists for features, limitations, dependencies
- Numbered lists for step-by-step procedures
- Bold for system names, service names, and critical warnings on first mention
- Each section should be self-contained and independently useful

### Anti-Hallucination Rules

Read the full rules at `references/anti-hallucination-rules.md`. Summary:

1. NEVER invent version numbers, URLs, or IP addresses
2. NEVER fabricate system names, service endpoints, or resource identifiers
3. NEVER guess deployment commands or configuration values
4. NEVER invent credential locations or access methods
5. NEVER add dependencies not found in the source documents
6. NEVER assume infrastructure details (regions, subscription IDs, resource groups)
7. Use "[To be confirmed]" / "[Noch zu bestätigen]" for ALL unknowns
8. Every component in Architecture must appear in Dependencies
9. Every credential referenced in Deployment must appear in Credentials section
10. Prefer omission over invention — a gap marker is infinitely better than wrong info in a handover doc

---

## Domain Adaptation Rule

**CRITICAL:** The sample excerpts in `references/sample-excerpts-*.md` show STRUCTURE and TONE only. ALL domain-specific content must come EXCLUSIVELY from the provided source data:

- System names: Use ACTUAL system names, never sample names
- Cloud resources: Use actual resource names, subscription IDs from source
- API endpoints: Use actual URLs from source
- Dependencies: Use actual versions from source
- Credentials: Use actual 1Password links and access lists from source

---

## File Paths (Relative to Skill Directory)

```
handover-document/
├── SKILL.md                              # This file
├── scripts/
│   └── generate_handover_doc.py          # Python DOCX generator (optional secondary output)
├── assets/
│   └── logos/
│       └── onethousand-icon-limeonblack-rounded.png  # DOCX cover page logo (optional)
├── references/
│   ├── section-templates-de.md           # German section prompts
│   ├── section-templates-en.md           # English section prompts
│   ├── anti-hallucination-rules.md       # Verification framework
│   ├── sample-excerpts-de.md             # German sample (structure/tone only)
│   └── sample-excerpts-en.md             # English sample (structure/tone only)
```

---

## Brand Guidelines (DOCX Only — Optional Secondary Output)

| Element | Font | Size | Color |
|---------|------|------|-------|
| Title page "handover" | Amsi Pro Narw Black | 48pt | White on #19A960 |
| Project name subtitle | Amsi Pro Narw Black | 24pt | White |
| Client attribution | Amsi Pro Narw Black | 18pt | White |
| H1 section headings | Amsi Pro Narw Black | 16pt | #19A960 |
| H2 subsection headings | Amsi Pro Narw Black | 14pt | #19A960 |
| H3 sub-subsection | Amsi Pro Narw Black | 12pt | #19A960 |
| Body text | Akkurat LL | 11pt | #2F2F2F |
| Code blocks | Courier New | 10pt | #2F2F2F on #F5F5F5 |
| TOC title | Amsi Pro Narw Black | 28pt | #19A960 |
| Footer page numbers | Akkurat LL | 10pt | #2F2F2F |
| Cover page background | — | — | #19A960 (Sharp Green) |
| Table headers | Akkurat LL Bold | 11pt | White on #19A960 |
| Table body | Akkurat LL | 10pt | #2F2F2F |
