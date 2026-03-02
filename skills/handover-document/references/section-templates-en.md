# Section Templates — English

These templates guide content generation for each section of the handover document. They define the expected structure, required elements, and writing patterns.

---

## 1. Project Overview & Background

**Template:**

Write a 3-4 paragraph section covering:

**Paragraph 1 — Client & Challenge:**
"{Client name}, a {industry descriptor}, faces the challenge of {specific problem with scale}. This process is {impact: time-intensive, error-prone, resource-consuming} and {business consequence}."

**Paragraph 2 — Solution:**
"A project was carried out to {goal: automate/extract/classify/optimize} {specific process}. Through close collaboration and iterative development, a functional {deliverable type: MVP, API, platform} was realized that {specific capability}."

**Paragraph 3 — Key Capabilities:**
"Specifically, fields such as {field 1}, {field 2}, and {field 3} are reliably {extracted/classified/processed}. This {reduces errors, saves time, frees resources}."

**Paragraph 4 (optional) — Quality System:**
"The solution includes {quality mechanism: traffic light system, confidence scoring, validation pipeline} that {how it works}. Additionally, {optional output: reports, dashboards, alerts} can be generated."

**Required elements:** Client name, industry, problem scale, solution type, specific capabilities, business impact
**Banned elements:** Generic AI partnership language, marketing claims without evidence

---

## 2. Project Timeline

**Template:**

Present as a structured sprint breakdown:

```
## Sprint 1 (CW {start} & {end})
**{Sprint objective — one sentence}**
- {Deliverable 1}
- {Deliverable 2}
- {Deliverable 3}

## Sprint 2 (CW {start} - {end})
**{Sprint objective — one sentence}**
- {Deliverable 1}
- {Deliverable 2}

## Test & Handover Phase (CW {start} - {end})
{Description of testing, adjustments, and handover activities}
```

**Required elements:** Sprint numbers with date ranges (calendar week preferred), objective per sprint, deliverables
**Pattern:** Use CW (Calendar Week) notation. Group related sprints if they share an objective.

---

## 3. Features & Workflows

**Template:**

One subsection per major feature:

```
### {Feature Name}
{What it does — 1-2 sentences with technical specifics}
{How it works — process flow or integration points}
{Value it adds — measurable benefit or capability unlocked}
```

For API-based solutions, include:
- Endpoint URL pattern
- Request/response format summary
- Authentication method

**Required elements:** All features from source, technical specifics, user-facing value
**Banned elements:** Features not in source, assumed capabilities

---

## 4. IP & Legal Considerations

**Template:**

```
### IP Ownership
{Status of IP ownership — who owns the code, models, data outputs}
{Reference to contract clause if available}
Client confirmation: {Confirmed by [name] on [date] / [To be confirmed]}

### License Compliance
| **Component** | **License** | **Type** | **Compliance Status** |
| --- | --- | --- | --- |
| {library name} | {MIT/Apache/GPL/etc.} | {Permissive/Copyleft} | {Compliant/Review needed} |

### Contractual Clauses
- **Non-compete:** {One-line summary or "See contract §X" / [To be confirmed]}
- **Preferred partner:** {One-line summary or [To be confirmed]}
- **Code sharing restrictions:** {Summary of Weitergabe restrictions / [To be confirmed]}
- **Client sign-off status:** {Confirmed via email on [date] / [To be confirmed]}

### Data Protection
- {GDPR measures taken}
- {Anonymization approach}
- {Data retention policy}
- {DPA status: signed/pending/not applicable}
```

**Required elements:** IP ownership status, license compliance table, clause summaries, data protection status
**Pattern:** Use `[To be confirmed]` liberally — this section is often incomplete at handover time. The structure matters more than completeness.
**CRITICAL:** Do NOT fabricate legal details. Reference contracts or mark as `[To be confirmed]`.

---

## 5. Data Sources

**Template:**

```
### {Data Source Name}
- **Type:** {PDF, CSV, API, Database, etc.}
- **Volume:** {count or range}
- **Format:** {format details, variations}
- **Quality:** {quality observations, known issues}
- **Access:** {how data was/is provided}
```

**Required elements:** All data sources from source, type, volume, format
**Pattern:** Be specific about format variations (e.g., "53 historical timesheets with highly varying layouts")

---

## 5. Development History

**Template per sprint:**

```
## Sprint {N} (CW {dates})
{Sprint objective — from timeline}

### Details
{Narrative of what was built/improved}

**{Component/Feature}** {verb: refined, implemented, developed}
- **Decision:** {What was decided and why}
- **Decision:** {Another decision}
- **Results:** {Metrics — before/after where available}

{Additional work items}

{Items deferred to next sprint and rationale}
```

**Required elements:** Per-sprint breakdown, decisions with rationale, metrics progression
**Pattern:** Track metric improvement across sprints. Use `**Decision:**` prefix for all decisions. Use `**Results:**` prefix for metrics.

---

## 6. Architecture

**Template:**

```
## Architecture Diagram
{Embedded image}

## System Architecture Description

### Main Workflow
1. {Step 1 — e.g., "A client app sends an HTTPS request with JSON payload to the Azure App Service via its private endpoint."}
2. {Step 2 — processing}
3. {Step 3 — auxiliary services}
4. {Step 4 — credential retrieval}
5. {Step 5 — response}

### Core Components
| **Name** | **Type** | **Description** |
| --- | --- | --- |
| {component-name} | {Azure App Service / OpenAI / etc.} | {What it does} |

### Connections (optional)
| **Source** | **Target** | **Method** | **Authentication** | **Protocol** |
| --- | --- | --- | --- | --- |
| {source} | {target} | {Private endpoint / VPN / etc.} | {Bearer token / API key / etc.} | {HTTPS} |
```

**Required elements:** Workflow description (numbered steps), component table
**Optional elements:** Connections table, private endpoints table (include if source data has network-level detail)

---

## 7. Dependencies & Libraries

**Template:**

```
### Main Dependencies
- OS {name} {version}
- {Language} {version} or newer
- {IaC tool} {version} or newer
- {VCS} {version} or newer

### OS-level Packages (if applicable)
- {package1}
- {package2}

### {Language} Packages
\```{language}
"{package1} == {version}",
"{package2} == {version}",
\```
```

**Required elements:** ALL dependencies from source with exact versions
**Banned elements:** Assumed versions, packages not in source

---

## 8. Deployment Instructions

**Template:**

```
### Cloud Infrastructure
{IaC approach description}

{Prerequisites — install steps with commands}

{How to review changes}
\```
{exact command}
\```

{How to apply changes}
\```
{exact command}
\```

### Code Deployment
{Deployment method description}

{Setup steps (numbered)}
1. {Step with command}
2. {Step with command}

{Deployment steps (numbered)}
1. {Commit changes}: `{exact command}`
2. {Push to remote}: `{exact command}`
3. {Credential retrieval instructions}
```

**Required elements:** Exact commands (copy-pasteable), portal URLs, credential locations
**Pattern:** Include expected prompts and known ignorable warnings
**Banned elements:** Assumed commands, guessed URLs

---

## 9. Known Limitations & Open Issues

**Template:**

```
- {Limitation 1 — specific and honest}
- {Limitation 2 — with context if needed}
- {Planned but not implemented feature — with reason}
- {Known edge case — with workaround if available}
```

**Required elements:** All limitations from source
**Pattern:** Be honest and specific. Better to flag a real limitation than to omit it.

---

## 10. Code Package

**Template:**

```
### Delivery Method
{How code is shared: zip file on SharePoint / GitHub repo / etc.}

### Access
{Link or URL}
Access granted to: {list of email addresses}

### Contents
{What's included — main application, infrastructure code, tests, etc.}
{What's excluded — internal scripts, notebooks, test data, etc.}

### Environment Variables
{How to obtain .env file — 1Password link, email, etc.}
```

**Required elements:** Delivery method, access details, content description
**Banned elements:** Actual credentials or secrets in the document

---

## 11. Credentials & Access

**Template per system:**

```
### {System/Service Name}
1. Secure link: {1Password share URL}
2. Access granted to: {list of email addresses}
3. Expires: {expiry date}
```

**Required elements:** All systems requiring credentials, secure access method, who has access
**CRITICAL:** NEVER include actual passwords, tokens, or API keys. Only links to secure stores.
**Pattern:** Group by category (Infrastructure, API, Deployment, Monitoring)

---

## 12. Recommendations & Next Steps

**Template:**

```
### Short-term
- {Immediate improvement 1}
- {Bug fix or optimization}

### Medium-term
- {Feature extension}
- {Additional integration}

### Long-term
- {Strategic vision}
- {Platform evolution}

### Maintenance
{Who handles ongoing support}
{SLA or support arrangement details}
```

**Required elements:** At least one recommendation per time horizon
**Pattern:** Be actionable — each recommendation should be specific enough to become a task
