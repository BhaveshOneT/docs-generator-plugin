# Scope Document Section Templates - English

Professional reference guide for writing each section of a scope document in English. Based on RVT scope document style: partnership-focused, evidence-based, and professional tone.

---

## 1. Initial Context

**Purpose**: Establish the business problem, justify the PoC approach, and demonstrate what was validated during the hackathon.

### Template Patterns

#### Pattern A (Discovery-focused)
"During the hackathon conducted on {{DATE}}, {{CLIENT}} and One Thousand explored {{TOPIC}}. The exploration revealed {{HACKATHON_FINDING}}. This PoC builds on those validated assumptions to deliver a production-ready {{USE_CASE}} solution."

#### Pattern B (Challenge-focused)
"{{CLIENT}} currently faces a significant challenge with {{BUSINESS_PROBLEM}}. This results in {{IMPACT_OF_PROBLEM}}. During the hackathon on {{DATE}}, we demonstrated that {{HACKATHON_FINDING}} can address this gap. This PoC scope outlines how to develop a complete solution for {{USE_CASE}}."

#### Pattern C (Opportunity-focused)
"The hackathon on {{DATE}} with {{CLIENT}} identified an opportunity to {{OPPORTUNITY}}. Our exploration showed that {{HACKATHON_FINDING}}. This PoC will transform that proof-of-concept into a scalable, integrated solution for {{USE_CASE}}."

### Key Phrases to Use
- "During the hackathon, we validated..."
- "The exploration revealed..."
- "This demonstrates the feasibility of..."
- "Building on this foundation, this PoC will..."
- "One Thousand and {{CLIENT}} explored the intersection of..."

### Key Phrases to Avoid
- "We will explore whether..." (suggests uncertainty, not validation)
- "We hope to demonstrate..." (passive, not confident)
- "Allegedly, the system could..." (informal for professional documents)
- Vague references to "requirements" without context

### Structure
1. Opening sentence: What was explored during the hackathon
2. Middle sentences: Key finding from the hackathon, why it matters
3. Closing sentence: How this PoC builds on that foundation

### Variable Placeholders
- `{{CLIENT}}`: Client company name
- `{{DATE}}`: Hackathon date (e.g., "March 15-16, 2024")
- `{{TOPIC}}`: What the hackathon explored (e.g., "AI-powered document classification")
- `{{USE_CASE}}`: The specific use case (e.g., "invoice processing automation")
- `{{HACKATHON_FINDING}}`: Key validated finding (e.g., "a rule-based classifier can accurately categorize documents with 85% accuracy using only the invoice header")
- `{{BUSINESS_PROBLEM}}`: The challenge {{CLIENT}} faces
- `{{IMPACT_OF_PROBLEM}}`: How it affects them (time, cost, quality)

### Length Guidelines
- 2-3 sentences minimum
- 5-6 sentences maximum
- 150-250 words typical range

---

## 2. In-Scope Features

**Purpose**: Describe exactly what will be built, with sufficient detail to be binding.

### Template Patterns

#### Section Header Format
"### 2.1 [Feature Name]"

#### Paragraph Introduction Pattern
"[Feature Name] encompasses the ability to {{ACTION}} by {{METHOD}}. This feature will {{BENEFIT}}. The implementation includes [specific components or integrations]."

#### Multi-part Feature Pattern
"2.1 [Feature Name] will deliver three core capabilities:
- [Capability A]: [one-sentence description]
- [Capability B]: [one-sentence description]
- [Capability C]: [one-sentence description]

The feature includes [additional context]. {{CLIENT}} will be able to [tangible outcome]."

### Deliverables Format
After each feature description, include bullet points for concrete deliverables:

```
**Deliverables:**
- [Specific component/function]
- [Technical implementation detail]
- [Integration point]
- [User-facing capability]
```

### Common AI Features - Writing Patterns

#### Data Extraction Feature
"2.1 Automated Data Extraction will enable the system to identify and extract key information from [document type]. Using [extraction method], the system will parse [document structure] and populate [target format] with {{ACCURACY_RATE}}% accuracy. {{CLIENT}} users will be able to [user action], reducing manual data entry time by an estimated {{TIME_SAVED}}."

**Deliverables:**
- Extraction model trained on [data source]
- API endpoint accepting [input format]
- Output schema matching {{CLIENT}}'s database structure
- Confidence scoring for extracted values
- Human-in-the-loop review interface

#### Classification Feature
"2.2 Document Classification will automatically categorize [document type] into [number] predefined categories. The classifier uses [method] and achieves [accuracy metric] based on [training data source]. This enables {{CLIENT}} to [workflow improvement], eliminating [pain point]."

**Deliverables:**
- Classification model with [number] output categories
- Confidence thresholds for automatic vs. manual review
- API integration with [system name]
- Admin dashboard to view classification accuracy metrics
- Process for updating categories

#### Chatbot/Conversational Feature
"2.3 Intelligent Query Interface will enable {{CLIENT}} staff to ask natural language questions about [domain]. The system will understand [query types] and retrieve [information source], presenting responses in [format]. This reduces reliance on [manual process]."

**Deliverables:**
- Natural language understanding model for [domain]
- Integration with [knowledge source/database]
- Conversation context management
- Fallback to human agent when [condition]
- User satisfaction feedback mechanism

#### Dashboard/Analytics Feature
"2.4 Executive Dashboard will provide real-time visibility into [metrics]. The dashboard will display [key metrics], with drill-down capability to [detail level]. {{CLIENT}} leadership can monitor [business objective] and identify [improvement opportunity]."

**Deliverables:**
- Real-time data connection to [data source]
- Visualization components for [specific metrics]
- Configurable time range filters
- Export capability to [format]
- [Number] pre-built report templates

#### API Integration Feature
"2.5 Integration with [External System] will enable seamless data flow between [System A] and [System B]. The integration will [synchronize/exchange/pull] [data type] on [frequency], ensuring {{CLIENT}} maintains a single source of truth for [critical data]."

**Deliverables:**
- OAuth/API authentication configuration
- Data transformation logic from [Source Format] to [Target Format]
- Scheduled sync job with error handling and retry logic
- Audit log of all data transfers
- Documentation of field mappings

### Key Phrases to Use
- "The feature will enable {{CLIENT}} to..."
- "This implementation includes..."
- "Deliverables for this feature are..."
- "The system will automatically..."
- "{{CLIENT}} users can..."

### Key Phrases to Avoid
- "We will try to..." (uncertain)
- "The feature might..." (hedge language)
- "Best effort to..." (non-binding)
- Overly technical jargon without explanation

### Structure Per Feature
1. Opening sentence: What the feature does in business terms
2. Technical details: How it works, accuracy, integrations
3. Benefit statement: What improves for {{CLIENT}}
4. Deliverables: Specific, measurable outputs

### Variable Placeholders
- `{{ACTION}}`: What users can do (e.g., "extract vendor information from invoices")
- `{{METHOD}}`: How it works (e.g., "a machine learning model trained on historical data")
- `{{BENEFIT}}`: Why it matters (e.g., "reducing processing time from 2 hours to 5 minutes per document")
- `{{ACCURACY_RATE}}`: Expected performance (e.g., "95%")
- `{{TIME_SAVED}}`: Time benefit
- `{{COMPONENT}}`: Technical component (e.g., "extraction API")

### Length Guidelines
- Minimum 3 paragraphs per major feature
- 1-2 paragraphs for minor features
- 200-400 words per feature typical range
- Bullet lists of 4-8 items per deliverables section

---

## 3. Out-of-Scope Features

**Purpose**: Explicitly state what is NOT included to prevent scope creep.

### Template Pattern

Use a dash-separated list format:

```
## 3. Out-of-Scope Features

The following items are explicitly excluded from this PoC scope:

— **[Feature Name]**: [Brief reason why excluded or deferred]
— **[Feature Name]**: [Brief reason]
— **[Feature Name]**: [Brief reason]
```

### Common Out-of-Scope Items

#### Production Deployment
"— **Production Environment Deployment**: While the PoC will be fully functional, deployment to {{CLIENT}}'s production infrastructure, including load balancing, disaster recovery, and production security hardening, is outside this scope. A separate deployment engagement would be required for production rollout."

#### Data Migration
"— **Historical Data Migration**: The PoC will be configured to accept new data and process it correctly. Migration of {{CLIENT}}'s existing historical data from [legacy system] is not included. A separate data migration project may be required before production launch."

#### User Training & Change Management
"— **End-User Training**: This engagement does not include developing training materials or conducting user training sessions. {{CLIENT}} will be responsible for end-user training based on provided documentation and training environment access."

#### Security Audit
"— **Security Audit & Compliance Certification**: While the solution will follow security best practices, a formal security audit or compliance certification (e.g., SOC 2, ISO 27001) is not included in this scope."

#### Load Testing & Performance Optimization
"— **Load Testing & Performance Optimization**: The PoC will be tested under typical usage patterns. Comprehensive load testing for [number] concurrent users and optimization for peak performance is deferred to a post-PoC engagement."

#### Custom Integrations (Additional)
"— **Integration with [Third-party System]**: This PoC includes integration with [System A]. Custom integrations with [System B] and [System C] are not included and would require a separate scope."

#### Multi-language Support
"— **Multi-language Localization**: The PoC will be delivered in English. Translation to [other languages] and localization for regional markets is not included."

#### Advanced Analytics
"— **Advanced Predictive Analytics**: The PoC includes basic dashboards and reporting. Machine learning-based predictive models for [use case] are deferred to a future phase."

#### Mobile Application
"— **Mobile Application**: This PoC focuses on web-based access. Development of native mobile applications for iOS and Android is not included."

#### Custom Hardware Integration
"— **Custom Hardware Integration**: The solution will run on standard server infrastructure. Integration with [specific hardware/devices] is not included."

### Key Phrases to Use
- "explicitly excluded from this scope"
- "outside this PoC"
- "deferred to a future phase"
- "not included in this engagement"
- "may be required in a subsequent project"

### Key Phrases to Avoid
- "We won't do..." (too informal)
- "Maybe later..." (vague)
- "Probably out of scope..." (uncertain)
- Just listing items without explanation

### Structure Per Item
1. Feature/item name in bold
2. Clear reason why it's excluded or deferred
3. When applicable, suggest when it might be addressed

### Variable Placeholders
- `{{CLIENT}}`: Client name
- `{{SYSTEM}}`: System names
- `{{LEGACY_SYSTEM}}`: The system being replaced/integrated with
- `{{TIME_PERIOD}}`: Timeline if applicable

### Length Guidelines
- 1 sentence per out-of-scope item
- 40-80 words per item
- List of 4-8 items typical
- Total section 200-400 words

---

## 4. Architecture Diagram

**Purpose**: Provide visual representation of the proposed system design with brief explanatory context.

### Template Patterns

#### Simple Architecture Introduction
"The following architecture diagram illustrates the proposed system design for {{USE_CASE}}. The design separates concerns across three layers: [Layer 1], [Layer 2], and [Layer 3]. This architecture ensures [benefit], maintains {{CLIENT}}'s data governance standards, and provides clear separation between [concern A] and [concern B]."

#### Integration-focused Architecture Introduction
"The proposed architecture for {{USE_CASE}} integrates {{CLIENT}}'s existing systems with new AI capabilities. [System A] serves as the primary data source, [System B] maintains the single source of truth, and the new [component] processes and enriches data before [outcome]. This approach ensures {{CLIENT}} maintains control over [critical aspect] while leveraging [technology] for [benefit]."

#### Multi-component Architecture Introduction
"The solution comprises four main components: (1) [Component A] for [function], (2) [Component B] for [function], (3) [Component C] for [function], and (4) [Component D] for [function]. Data flows from [source] through [processing] and results in [outcome]. This design enables [benefit] and minimizes [risk]."

### Key Elements to Describe After Diagram
- Primary data flows and their direction
- System boundaries and security zones
- Third-party integrations and their role
- Where {{CLIENT}}'s data is stored and processed
- How the system handles [critical process]

### Key Phrases to Use
- "The architecture consists of..."
- "Data flows from [source] to [destination]..."
- "This design ensures..."
- "[Component] is responsible for..."
- "The system integrates with [external service]..."

### Key Phrases to Avoid
- "We might use..." (uncertain, belongs in future phases)
- "The diagram shows what we'll probably build..." (hedge language)
- Unexplained technical terms without business context

### What NOT to Include in Architecture Section
- Implementation details that belong in feature descriptions
- Specific tool/library choices (those go in technical specifications)
- Deployment architecture (that's separate from logical design)
- Code snippets or pseudocode

### Structure
1. Opening sentence: What the diagram shows
2. Layer/component overview: Main building blocks and their purpose
3. Data flow explanation: How information moves through the system
4. Key benefits: Why this architecture was chosen

### Variable Placeholders
- `{{USE_CASE}}`: The specific use case (e.g., "invoice automation")
- `{{BENEFIT}}`: Why this architecture matters (e.g., "scalability and maintainability")
- `{{COMPONENT}}`: System component name

### Length Guidelines
- Introduction text: 150-250 words
- Include actual architecture diagram (Miro, Lucidchart, or similar)
- Keep diagram text minimal and clear

---

## 5. Prerequisites from {{CLIENT}}

**Purpose**: Clearly state what the client must provide for the PoC to succeed.

### Template Patterns

#### Standard Prerequisites Format
```
## 5. Prerequisites from {{CLIENT}}

For this PoC to proceed successfully, {{CLIENT}} must provide:

- [Prerequisite item] - [description] - {{STATUS}}
- [Prerequisite item] - [description] - {{STATUS}}
- [Prerequisite item] - [description] - {{STATUS}}
```

#### Prerequisites with Status Indicators
```
**Data Access Prerequisite:**
- Access to [System/Database Name] - Read access to [specific tables/endpoints] required for [purpose] - Status: {{STATUS}}
  - {{CLIENT}} Owner: [Role]
  - Timeline: Should be available by [date]
  - Effort to provide: [estimate, e.g., "1-2 hours"]

**Domain Expert Prerequisite:**
- [Number] hours per week domain expert availability - For requirements clarification, terminology validation, and [specific use case]. Minimum [X] hours per sprint - Status: {{STATUS}}
  - {{CLIENT}} Owner: [Name/Role]
  - Suggested meeting cadence: [frequency]

**Infrastructure Prerequisite:**
- [Infrastructure requirement] - {{CLIENT}} must provide [description]. Estimated capacity: [spec] - Status: {{STATUS}}
  - {{CLIENT}} Owner: [Role]
  - Timeline: Ready by [date]
```

### Common Prerequisites

#### API Access
"- **API Access to [System Name]**: Read and write access to {{CLIENT}}'s [System Name] API, with credentials to authenticate as [integration user]. Required for [data source/destination] operations. Status: {{STATUS}}"

#### Sample Data / Training Data
"- **Representative Sample Data**: [Number] sample records from [system/process] containing [data types]. This data will be used to [train models/configure extraction rules/demonstrate functionality]. Status: {{STATUS}}"

#### Domain Expert Availability
"- **Subject Matter Expert Availability**: [X] hours per week availability from {{CLIENT}}'s [Domain] expert for requirements validation, test case review, and terminology clarification. Recommended meeting frequency: [cadence]. Status: {{STATUS}}"

#### Test Environment
"- **Test Environment Access**: Dedicated test instance of [System Name] with [specifications] where One Thousand can [install/test/integrate] without affecting production. Status: {{STATUS}}"

#### IT Infrastructure Access
"- **IT Infrastructure Access**: Network access to [systems], database connection string for [database], and appropriate firewall rule allowances for [services]. Status: {{STATUS}}"

#### Business Process Documentation
"- **Current Process Documentation**: Documentation or videos of {{CLIENT}}'s current [process] including [specific steps]. This will inform our [understanding/requirements/test cases]. Status: {{STATUS}}"

#### Approval Process / Sign-offs
"- **Stakeholder Approval**: {{CLIENT}} will designate a [role] who can approve [decisions/changes] during the PoC. One Thousand requires documented decisions by [date] on [topics]. Status: {{STATUS}}"

#### Feedback & Testing Resources
"- **User Testing Participation**: [Number] {{CLIENT}} end-users available to participate in [testing activities/UAT] on [frequency]. Status: {{STATUS}}"

### Status Indicators
- ✓ Confirmed - Client has confirmed availability
- ⏳ In Progress - Client is working to provide
- ⚠ At Risk - Potential blockers identified
- ❌ Not Yet Addressed - Still to be discussed

### Key Phrases to Use
- "{{CLIENT}} must provide..."
- "Required for {{USE_CASE}} to..."
- "Owner: {{CLIENT}} [role]"
- "Timeline: Available by [date]"
- "Estimated effort to provide: [estimate]"

### Key Phrases to Avoid
- "We hope {{CLIENT}} can..." (passive)
- "Ideally, {{CLIENT}} would..." (uncertain)
- "If possible..." (hedge language)

### Structure
1. Grouping by category (Data, Infrastructure, People, Resources)
2. Specific requirement description
3. Why it's needed (purpose)
4. Current status
5. Responsible {{CLIENT}} party
6. Timeline for availability

### Variable Placeholders
- `{{CLIENT}}`: Client company name
- `{{STATUS}}`: ✓ Confirmed, ⏳ In Progress, ⚠ At Risk, ❌ Not Addressed
- `{{USE_CASE}}`: The specific use case
- `{{ROLE}}`: Job title at {{CLIENT}}

### Length Guidelines
- 1 line per straightforward prerequisite
- 2-3 lines per complex prerequisite
- Total list: 6-12 items typical
- Total section: 300-500 words

---

## 6. High-Level Sprint Design

**Purpose**: Outline the development timeline, deliverables per sprint, and key milestones.

### Template Patterns

#### Standard Sprint Format
```
## 6. High-Level Sprint Design

The PoC will be delivered over {{SPRINT_COUNT}} sprints of {{SPRINT_LENGTH}} weeks each.

### Sprint 0: Foundation & Setup ({{DURATION}})
**Objective**: Establish development environment, integrate data sources, and validate technical approach.

**Key Activities**:
- [Activity description]
- [Activity description]
- [Activity description]

**Deliverables**:
- [Specific working component]
- [Integration/configuration]
- [Documentation or artifact]

**Success Criteria**:
- [Measurable condition]
- [Measurable condition]

---

### Sprint 1: [Feature Name] ({{DURATION}})
**Objective**: [What will be accomplished in one sentence]

**Key Activities**:
- [Activity]
- [Activity]

**Deliverables**:
- [Feature component]
- [Testing/validation artifact]

**Success Criteria**:
- [Feature works as specified]
- [Performance threshold met]
```

#### Multi-Sprint Feature Delivery
"### Sprint 1-2: [Feature Name] Development ({{DURATION}})"

### Common Sprint Types

#### Sprint 0 / Foundation Sprint
```
### Sprint 0: Foundation & Setup (1 week)
**Objective**: Prepare development infrastructure and validate technical assumptions from the hackathon.

**Key Activities**:
- Configure development environment and code repository
- Establish data connections to {{CLIENT}}'s [System Name]
- Validate access to [data sources] and confirm data structure assumptions
- Conduct technical architecture review with {{CLIENT}} stakeholders
- Set up logging, monitoring, and local testing framework

**Deliverables**:
- Development environment fully operational and documented
- Confirmed data integration working end-to-end
- Technical design document reviewed and approved by {{CLIENT}}
- Definition of done standards established

**Success Criteria**:
- Development team can build and test features locally
- Data flows correctly from {{CLIENT}} systems to development environment
- Technical risks identified and mitigation plans in place
- {{CLIENT}} technical stakeholders have approved the approach
```

#### Feature Implementation Sprint
```
### Sprint 1: [Feature Name] Core Functionality (1 week)
**Objective**: Deliver the core functionality for [feature], including data processing and user interface.

**Key Activities**:
- Implement [specific component] based on [approach]
- Create [user interface/API endpoints] for {{CLIENT}} to [user action]
- Build [supporting infrastructure] for [purpose]
- Develop unit tests achieving [coverage percentage]
- Conduct internal code review

**Deliverables**:
- Working [feature] accessible via [interface]
- Unit test suite with [X%] code coverage
- API documentation (if applicable)
- Internal testing report with known limitations

**Success Criteria**:
- Feature [specific criteria]
- Performance meets [threshold]
- Code passes quality gates
- {{CLIENT}} technical team can review and test
```

#### Testing & Refinement Sprint
```
### Sprint 2: Testing, Refinement & Integration (1 week)
**Objective**: Validate [feature] against {{CLIENT}} requirements, fix defects, and prepare for handover.

**Key Activities**:
- Conduct {{CLIENT}} user acceptance testing with [participants]
- Document and fix identified issues
- Refine [specific areas] based on feedback
- Prepare training materials and user documentation
- Performance testing and optimization

**Deliverables**:
- Updated feature with all UAT-identified defects resolved
- User documentation and [type] training materials
- Performance test results and optimization report
- Known issues log (if any) with workarounds

**Success Criteria**:
- {{CLIENT}} approves feature for production
- All critical and high-priority issues resolved
- Documentation is complete and reviewed
- No open blockers for deployment
```

#### Final Sprint (Handover)
```
### Sprint 3: Final Testing, Documentation & Handover ({{DURATION}})
**Objective**: Conduct final quality assurance, prepare operational documentation, and transfer knowledge to {{CLIENT}}.

**Key Activities**:
- End-to-end system testing in {{CLIENT}}'s test environment
- Create [operational documentation] for {{CLIENT}} IT team
- Conduct [support team] training on [system operations/troubleshooting]
- Prepare production deployment runbook
- Create [knowledge transfer artifacts]

**Deliverables**:
- Final quality assurance report
- Operational runbooks and troubleshooting guides
- Training materials for [support/operations/end-users]
- Production deployment plan and checklist
- Knowledge transfer documentation

**Success Criteria**:
- {{CLIENT}} support team can operate and troubleshoot the system
- All documentation is complete and reviewed
- Zero blocker-level defects remaining
- {{CLIENT}} ready for production handover
```

### Key Phrases to Use
- "Sprint [N] focuses on..."
- "Deliverables for this sprint:"
- "Success criteria include..."
- "Key milestones: [date], [date]..."
- "By the end of Sprint [N], {{CLIENT}} will have..."

### Key Phrases to Avoid
- "We'll try to..." (uncertain)
- "Depending on issues..." (vague)
- "Hopefully we'll complete..." (unprofessional)

### Structure Per Sprint
1. Sprint title and duration
2. Objective statement (one sentence)
3. Key activities (3-5 items)
4. Specific deliverables (3-5 items)
5. Clear success criteria (2-3 measurable items)

### Variable Placeholders
- `{{SPRINT_COUNT}}`: Total number of sprints (e.g., "3")
- `{{SPRINT_LENGTH}}`: Length of each sprint (e.g., "1-week")
- `{{DURATION}}`: Duration of this sprint (e.g., "1 week")
- `{{FEATURE_NAME}}`: Feature being built
- `{{CLIENT}}`: Client name

### Length Guidelines
- Sprint 0: 200-300 words
- Feature sprints: 250-350 words each
- Final sprint: 250-350 words
- Total section: 1000-1500 words for 3-4 sprint PoC

---

## 7. Conclusion

**Purpose**: Close professionally, reinforce partnership, and set stage for next steps.

### Template Patterns

#### Partnership-focused Conclusion
"One Thousand is excited to partner with {{CLIENT}} on this {{USE_CASE}} initiative. We believe the proposed scope represents an achievable, high-impact PoC that will [benefit]. Our team brings [relevant expertise], and we're committed to delivering a solution that [addresses stated goal]. We look forward to [next step] and to supporting {{CLIENT}}'s [strategic objective] through this engagement."

#### Value-focused Conclusion
"This PoC will enable {{CLIENT}} to [key benefit]. By delivering [outcome], {{CLIENT}} will be positioned to [strategic advantage]. One Thousand's team is ready to begin work on [date]. We're confident that the proposed scope is achievable and will deliver measurable value by the completion of the PoC in [timeframe]."

#### Action-oriented Conclusion
"One Thousand is ready to commence the {{USE_CASE}} PoC. The next step is to [specific next action] by {{CLIENT}} by [date], which will allow us to start on [date]. We will formally kick off with {{CLIENT}} leadership and technical team on [date]. Please confirm your availability and let us know if you have any questions about this scope document. We're excited to get started."

### Key Elements to Include
- Restatement of the value proposition
- Confirmation of readiness to proceed
- Reference to the next step or kickoff
- Positive, forward-looking tone
- Contact information or next meeting date

### Key Phrases to Use
- "One Thousand is excited to..."
- "This PoC will enable {{CLIENT}} to..."
- "We're committed to..."
- "The next step is..."
- "We look forward to..."

### Key Phrases to Avoid
- "We hope this works..." (uncertain)
- "Fingers crossed..." (informal)
- "If everything goes well..." (hedge language)
- Unsupported optimism about outcomes

### Structure
1. Opening: Partnership affirmation and value statement
2. Middle: Restatement of key benefits
3. Closing: Next steps and readiness confirmation

### Variable Placeholders
- `{{CLIENT}}`: Client company name
- `{{USE_CASE}}`: The specific use case
- `{{BENEFIT}}`: Key benefits from this PoC
- `{{DATE}}`: Next milestone date (kickoff, document sign-off, etc.)
- `{{TIMEFRAME}}`: PoC completion timeframe

### Length Guidelines
- 3-4 sentences minimum
- 4-5 sentences maximum
- 150-250 words typical range

### Example Full Conclusion
"One Thousand is excited to partner with {{CLIENT}} on this invoice automation initiative. This PoC will enable {{CLIENT}} to reduce invoice processing time from 45 minutes to under 10 minutes per document, dramatically improving accounts payable efficiency. We're committed to delivering a robust, thoroughly tested solution that {{CLIENT}} can confidently deploy to production by the end of Q2.

The next step is for {{CLIENT}} to confirm the prerequisites outlined in Section 5 and approve this scope document. We're ready to kick off on March 22nd and deliver measurable impact within four weeks. Please let us know if you have any questions or would like to discuss any aspect of the proposed scope."

---

## Writing Style Guidelines for All Sections

### Tone
- Professional but not stuffy
- Confident and capability-focused
- Partnership-oriented (use "we" and "our")
- Benefit-focused (emphasize {{CLIENT}} outcomes)
- Evidence-based (everything traces to the hackathon or stated requirements)

### Structure
- Clear section headers with numbering
- Topic sentences at the start of paragraphs
- Bullet points for lists of related items
- Short paragraphs (3-5 sentences typical)
- Avoid walls of text

### Language
- Active voice preferred: "The system will extract..." not "Extraction will be performed..."
- Specific and concrete language
- Define technical terms on first use
- Use consistent terminology throughout (don't vary between "extract," "parse," "identify" for the same concept)
- Avoid marketing jargon or unsupported superlatives

### What Makes a Good Scope Document Section
- ✓ Every claim traces to the hackathon documentation or user notes
- ✓ Features are described with enough detail to be binding
- ✓ Client benefits are explicitly stated
- ✓ Prerequisites are clear and actionable
- ✓ Timeline and deliverables are specific
- ✓ Out-of-scope items prevent scope creep
- ✓ No unexplained jargon or technical acronyms
- ✓ Consistent use of terminology
- ✓ Benefits outweigh effort (apparent in tone)

### Common Errors to Avoid
- ✗ Vague language: "We'll do our best," "hopefully," "we'll try"
- ✗ Unsubstantiated claims: "This will save 50% time" (without evidence)
- ✗ Invented details: features not in the hackathon, made-up timeline, fictional metrics
- ✗ Inconsistent terminology: switching between "user," "operator," "administrator"
- ✗ Missing prerequisites: assuming client has systems/resources without stating
- ✗ Scope creep: features that are out-of-scope not explicitly listed as such
- ✗ Undefined acronyms: using "DAG," "ETL," "RAG" without explaining first use
