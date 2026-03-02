# Sample Excerpts — English

**WARNING:** These excerpts show STRUCTURE and TONE only. ALL domain-specific content (company names, system names, metrics, URLs) must come EXCLUSIVELY from the provided source documents. NEVER carry over terms or details from these examples into the actual document.

---

## Example: Project Overview & Background

> **Example Corp**, a leading provider in personnel and project management, currently faces the challenge of manually processing approximately 600 timesheets monthly in varying formats. This process is not only time-intensive but also error-prone and ties up valuable capacity that could be better utilized elsewhere.
>
> Against this background, a project was carried out with the goal of automatically extracting relevant data from digitized timesheets, converting them into structured JSON files, and preparing them for integration into the target system. Through close collaboration and iterative development, a functional MVP was realized.
>
> Specifically, fields such as date, hours worked, and absences are reliably detected and standardized. This minimizes errors, reduces manual effort, and frees up valuable time resources.
>
> The solution includes an API through which timesheets can be submitted, automatically read, and returned in JSON format. Additionally, a traffic light system (green, yellow, red) evaluates extraction quality and makes potential issues transparently visible.

**Note the tone:** Factual, specific, problem-oriented. Starts with the client's problem, not the partnership.

---

## Example: Development History (one sprint)

> ## Sprint 2 (CW 34 & 35)
>
> Refinement of validation logic and classification (traffic light system: Green/Yellow/Red).
>
> ### Details
>
> **Validation logic** and classification further developed.
>
> - **Results:** Validation was increased from 46% to 79% in this sprint.
>
> **VPN connection** for infrastructure established. This connection was initially set up for one user.
>
> **Decision:** Connecting our infrastructure to the client environment proved complex. Together with the client, we successfully implemented their required setup steps.
>
> Additionally, validation needed to reach 90%. Since hackathon results dropped significantly under stricter rules (from 63% to 14%), we invested additional effort to increase the validation rate.
>
> To maintain clear focus, PNG image generation was deferred to Sprint 3.

**Note the patterns:**
- `**Decision:**` prefix for decisions
- `**Results:**` prefix for metrics
- Metric progression across sprints (14% → 46% → 79%)
- Deferred items with rationale

---

## Example: Architecture

> ### Main Workflow
>
> 1. A client app sends an HTTPS request with JSON payload to the **Azure App Service** via its private endpoint. The request contains data such as PDF/document binary data, filename, consultant list, etc.
>
> 2. The **Azure App Service** uses **Azure OpenAI** and **Azure Document Intelligence** to extract timesheet details from the given file.
>
> 3. The **Azure App Service** sends telemetry and logs to **Application Insights** and the **Log Analytics workspace** for monitoring purposes.
>
> 4. The **Azure App Service** retrieves credentials from **Azure Key Vault** to access various services.
>
> 5. The **Azure App Service** sends back the HTTPS response with JSON payload containing extracted fields, matched consultant, and optional report.
>
> ### Core Components
>
> | **Name** | **Type** | **Description** |
> | --- | --- | --- |
> | example-webapp | Azure App Service | API endpoint |
> | example-openai | Azure OpenAI | LLM endpoint for data extraction |
> | example-docint | Azure AI Services | Document Intelligence endpoint |
> | example-vault | Azure Key Vault | Managed credentials |
> | example-appi | Azure Application Insights | Monitoring |
> | example-law | Azure Log Analytics | Log storage |

**Note the patterns:**
- Numbered steps for workflow
- Bold system names on first mention
- Table format for components (Name | Type | Description)

---

## Example: Deployment Instructions

> ### Cloud Infrastructure
>
> The cloud infrastructure is declared as Infrastructure-as-Code in Terraform (see /terraform folder).
>
> Before making any changes:
>
> 1. Install Terraform: https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
> 2. Download terraform.tfstate and terraform.tfvars via a secure channel and place them in the terraform folder.
> 3. Navigate to the terraform folder and initialize the project:
>
> ```
> cd terraform
> terraform init
> ```
>
> After modifying infrastructure code:
>
> ```
> terraform plan -var-file="terraform.tfvars"
> ```
>
> Review the list of changes. Once confirmed:
>
> ```
> terraform apply -var-file="terraform.tfvars"
> ```

**Note the patterns:**
- Numbered steps with exact commands
- Code blocks for ALL commands
- Prerequisites first, then execution
- Portal links where relevant

---

## Example: Credentials & Access

> ### Terraform State & Variables
>
> 1. Secure link: https://share.1password.com/s#EXAMPLE
> 2. Access granted to: name1@client.com, name2@client.com
> 3. Expires: 10 Nov 2025
>
> ### API Endpoint & Bearer Token
>
> 1. Secure link: https://share.1password.com/s#EXAMPLE
> 2. Access granted to: name1@client.com, name2@client.com
> 3. Expires: 10 Nov 2025

**Note the patterns:**
- Consistent structure per system (link, access, expiry)
- NEVER include actual credentials in the document
- 1Password share links as preferred method

---

## Example: Dependencies & Libraries

> ### Main Dependencies
>
> - OS Linux
> - Python 3.11 or newer
> - terraform v1.13 or newer
> - git 2.50 or newer
>
> ### OS-level Packages (Linux)
>
> - libcairo2
> - libpango-1.0-0
> - ghostscript
> - poppler-utils
>
> ### Python Modules
>
> ```python
> "fastapi == 0.115.12",
> "gunicorn == 23.0.0",
> "openai == 1.77.0",
> "pandas == 2.2.3",
> "uvicorn == 0.34.2",
> ```

**Note the patterns:**
- Grouped by category (Main, OS-level, Language)
- Exact version pinning with `==` operator
- Code block for language packages

---

## Example: Known Limitations

> - The system currently supports PDF and Word document formats only; image-based timesheets (scans without OCR pre-processing) are not supported
> - Multi-page timesheets spanning more than 3 months may show reduced accuracy in date extraction
> - The consultant matching algorithm requires exact name matches; partial or nickname matches are flagged as "yellow" for manual review
> - Batch processing of more than 50 timesheets simultaneously has not been load-tested

**Note the patterns:**
- Specific and honest
- Each limitation includes enough context to understand the scope
- No generic filler ("the system has some limitations")
