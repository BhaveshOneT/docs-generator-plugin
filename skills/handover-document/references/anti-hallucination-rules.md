# Anti-Hallucination Verification Framework for Handover Documents

This framework ensures all generated handover content is grounded in source data. Handover documents have HIGHER accuracy requirements than other document types because they contain operational instructions, credentials, and deployment commands that will be acted upon directly.

**Principle:** In a handover document, a wrong detail is worse than a missing detail. A `[To be confirmed]` marker is infinitely safer than an incorrect deployment command, wrong IP address, or fabricated credential location.

---

## Verification Checks

### 1. Technical Accuracy Check (Weight: 30%)

Every technical detail must trace to a specific location in the source material.

**What to verify:**
- All version numbers (Python 3.11, terraform v1.13, etc.)
- All URLs and endpoints (portal URLs, API endpoints, repo URLs)
- All IP addresses and DNS names
- All resource names (Azure service names, database names, etc.)
- All commands (terraform, git, deployment commands)
- All file paths and directory structures
- All package names and version pins

**Action if fails:** Flag the detail and use `[To be confirmed]` marker. Ask the user to provide or verify.

### 2. Terminology Check (Weight: 20%)

System names, service names, and technical terms must match the source exactly.

**What to verify:**
- Cloud resource names match exactly (e.g., "secure-questax-webapp" not "questax-webapp")
- Service types are correct (e.g., "Azure App Service" not "Azure Web App")
- API endpoint paths are exact
- Database names, table names, field names match source
- Infrastructure terms match (e.g., "Private endpoint" not "Private link" if source says "endpoint")

**Common mistakes to catch:**
- Using generic Azure service names instead of the actual resource names
- Mixing up similar service types (App Service vs Function App)
- Shortening or abbreviating resource identifiers
- Using sample document terminology instead of actual project terms

**Action if fails:** Replace with correct terminology from source.

### 3. Completeness Check (Weight: 25%)

All required content must be present for the document to be a functional handover.

**What to verify:**
- All cloud components from the architecture appear in the component table
- All dependencies from the code appear in the dependencies section
- All credentials needed for deployment appear in the credentials section
- All deployment steps are complete (no gaps in the procedure)
- All data sources are listed
- Sprint history covers all sprints from timeline
- Cross-reference: every system in Architecture has credentials in Credentials section
- Cross-reference: every dependency mentioned in Deployment appears in Dependencies

**Action if fails:** Add the missing content from source data, or mark as `[To be confirmed]`.

### 4. Actionability Check (Weight: 25%)

Can someone follow this document to actually operate the solution?

**What to verify:**
- Deployment commands are copy-pasteable and complete
- Credential access instructions lead to actual credential stores
- Infrastructure setup is step-by-step with no implied knowledge
- Code package access instructions are complete
- Known limitations don't leave surprises
- Recommendations are specific enough to be actionable

**Action if fails:** Add missing operational detail or mark as `[To be confirmed]`.

---

## Anti-Hallucination Rules (Handover-Specific)

1. **NEVER invent version numbers** — If a requirements.txt isn't in source, mark as `[To be confirmed]`
2. **NEVER fabricate URLs or endpoints** — Use only URLs from source documents
3. **NEVER guess deployment commands** — A wrong command could break infrastructure
4. **NEVER invent IP addresses or DNS names** — Use only addresses from source
5. **NEVER fabricate credential locations** — Wrong credential info creates security risk
6. **NEVER assume infrastructure details** — Regions, SKUs, subscription IDs must come from source
7. **NEVER invent package dependencies** — Only list packages explicitly found in source
8. **NEVER assume team contacts** — Only list names explicitly found in source
9. **NEVER fabricate error codes or API schemas** — Use only schemas from source
10. **NEVER copy details from sample excerpts** — Sample documents are for STRUCTURE only
11. **Mark ALL unknowns explicitly** — Use `[To be confirmed]` (EN) or `[Noch zu bestätigen]` (DE)
12. **Cross-check sections** — Architecture ↔ Dependencies ↔ Deployment ↔ Credentials must be consistent
13. **Prefer omission over invention** — A shorter, accurate handover doc is better than a comprehensive fabricated one

---

## Scoring Dimensions

When scoring each section, evaluate these 5 dimensions (each 0-20 points):

1. **Source Grounding (0-20):** Is every claim traceable to the source document?
2. **Specificity (0-20):** Are names, versions, URLs, commands specific rather than generic?
3. **Completeness (0-20):** Does the section cover its full purpose per the template?
4. **Actionability (0-20):** Can someone act on this content? (deploy, access, troubleshoot)
5. **Anti-Hallucination (0-20):** Is the section free of invented details?

### Section-Specific Thresholds

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

---

## Gap Detection Patterns

When extracting content, actively look for these common gaps and ask the user for the specific missing document:

| Missing Content | Ask User For |
|----------------|--------------|
| No dependency list found | "Can you upload requirements.txt, package.json, or paste the dependency list?" |
| No deployment instructions | "Can you upload a deployment guide, README with deploy steps, or describe the process?" |
| No architecture diagram | "Can you upload the architecture diagram, or describe the system components so I can generate one?" |
| No credential information | "Can you provide 1Password vault links, credential locations, or access instructions?" |
| Incomplete sprint history | "I found sprint 1-2 details but nothing for sprint 3. Can you provide sprint 3 notes?" |
| No data source details | "What data sources does the project use? Types, volumes, formats?" |
| No known limitations | "Are there any known limitations, edge cases, or features not yet implemented?" |
| No team contacts | "Who are the key contacts on both the OT and client side?" |
