# Anti-Hallucination Rules for Architecture Diagram Generator

Strict operational rules to prevent AI hallucination and maintain factual accuracy in generated architecture diagrams. These rules are binding and override all other instructions when conflicts arise.

---

## Core Principle

**EVERY component, zone, data flow, and technical detail in the generated diagram must trace directly to source data (user input, project documentation, or meeting notes). No invented content under any circumstances.**

---

## Rule 1: Traceability Requirement

**Binding Rule**: Every element in the diagram must have a documented source.

### What requires a source:
- Component names and types
- Zone groupings and names
- Data flow connections and labels
- Technology choices (database type, API protocol, etc.)
- Architecture patterns (microservices, monolith, etc.)

### What constitutes a valid source:
- Direct statement from the user
- Content from project documentation provided by the user
- Extraction from existing architecture diagrams or descriptions
- User confirmation of a proposed element

### What is NOT a valid source:
- General knowledge about similar architectures
- Assumptions about what components "should" be there
- Best practices not mentioned by the user
- "This architecture typically includes..."

### Implementation:
```
Before including any element in the diagram:
1. Find the source: user message, document, or clarification
2. If source cannot be found: DO NOT INCLUDE the element
3. If source is ambiguous: ASK the user before including
```

---

## Rule 2: No Invented Components

**Binding Rule**: Do not add components that the user did not mention or confirm.

### Prohibited:
- Adding a "load balancer" because the architecture has multiple services
- Adding a "cache layer" because databases are present
- Adding a "monitoring service" because it's best practice
- Adding a "message queue" between services that weren't described as async

### Correct:
- Include only components explicitly mentioned by the user
- If you think a component is missing, ask: "Should the diagram include a cache/queue/etc.?"
- Recommend additional components in a note, not in the diagram itself

---

## Rule 3: No Invented Data Flows

**Binding Rule**: Do not create connections between components unless the user described the data flow.

### Prohibited:
- Connecting components because "they probably communicate"
- Adding bidirectional arrows when only one direction was described
- Inventing flow labels that weren't mentioned

### Correct:
- Only draw flows that were explicitly described
- If a connection seems implied but wasn't stated, ask the user
- Use the exact labels the user provided

---

## Rule 4: Preserve Exact Terminology

**Binding Rule**: Use the user's exact names for components, zones, and flows.

### Prohibited:
- User says "SQL Database" → Diagram shows "RDBMS" (generalised)
- User says "API Gateway" → Diagram shows "Reverse Proxy" (different concept)
- User says "ML Pipeline" → Diagram shows "AI Processing Engine" (rebranded)

### Correct:
- Copy exact names from user input
- If a name is unclear, ask for clarification
- If you need to abbreviate for display, keep the full name and use label line breaks

---

## Rule 5: No Invented Zone Groupings

**Binding Rule**: Only group components into zones that the user described.

### Prohibited:
- Creating a "Cloud" zone because some services sound cloud-based
- Splitting components into "Frontend" / "Backend" without user instruction
- Adding network boundary zones that weren't discussed

### Correct:
- Use only the zones the user specified
- If no zones are specified, leave components ungrouped
- Ask: "How would you like to group these components?" if grouping seems helpful

---

## Rule 6: Architecture Components Must Match Source

**Binding Rule**: The diagram must be a faithful representation of what was described, not an idealised version.

### Check for each element:
```
Component/Flow/Zone: [name]
Source: [exact user message or document reference]
If no source → DO NOT INCLUDE
If source is ambiguous → ASK the user
```

---

## Rule 7: Flag Gaps Explicitly

**Binding Rule**: When the architecture description is incomplete, flag gaps rather than filling them.

### When to flag:
- A component is mentioned but its connections aren't described
- A zone is mentioned but its members aren't listed
- A flow direction isn't specified
- Technology choices aren't stated

### How to flag:
- Ask the user for clarification before generating
- Do not generate with assumptions and hope for review

---

## What To Do When You're Tempted to Add Something

**Decision Tree**:
```
I want to add [component/flow/zone] because [reason]

Is it explicitly in the user's input?
├─ YES → Include it
└─ NO  → Did the user confirm it when asked?
    ├─ YES → Include it
    └─ NO  → Is it required for the diagram to make sense?
        ├─ YES → ASK the user before including
        └─ NO  → Do NOT include it
```

---

## Final Directive

**If in doubt about whether something was specified: ASK THE USER.**

The cost of asking a clarifying question is low.
The cost of hallucinating architecture components is high — it can lead to incorrect system designs, wrong infrastructure provisioning, and wasted engineering effort.

Always err on the side of asking rather than assuming.
