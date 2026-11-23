# 📦 SupplyChain Sentinel

## AI-Powered Supply Chain Crisis Management & Control Tower

SupplyChain Sentinel is a Streamlit-based supply chain crisis-management
application powered by a collaborative multi-agent AI workflow built
with CrewAI and Google Gemini.

The application is designed to help users investigate supply-chain
disruptions, understand their potential operational impact, and generate
a structured recovery strategy. It combines supply-chain datasets,
user-defined crisis scenarios, specialist AI agents, and an interactive
dashboard in one demonstration application.

------------------------------------------------------------------------

## Table of Contents

1.  [Project Overview](#-project-overview)
2.  [Problem Statement](#-problem-statement)
3.  [Objectives](#-objectives)
4.  [Key Features](#-key-features)
5.  [Multi-Agent Architecture](#-multi-agent-architecture)
6.  [Technology Stack](#-technology-stack)
7.  [Project Structure](#-project-structure)
8.  [How the Application Works](#-how-the-application-works)
9.  [Installation and Setup](#-installation-and-setup)
10. [Environment Configuration](#-environment-configuration)
11. [Running the Application](#-running-the-application)
12. [Using the Dashboard](#-using-the-dashboard)
13. [Supply-Chain Data](#-supply-chain-data)
14. [AI Tracing and Observability](#-ai-tracing-and-observability)
15. [Example Crisis Scenario](#-example-crisis-scenario)
16. [Troubleshooting](#-troubleshooting)
17. [Security Notes](#-security-notes)
18. [Limitations and Future
    Improvements](#-limitations-and-future-improvements)
19. [Contributing](#-contributing)
20. [License](#-license)

------------------------------------------------------------------------

## 🌐 Project Overview

Supply chains involve multiple connected activities, including sourcing,
supplier management, inventory planning, transportation, warehousing,
and delivery. A disruption in one part of the network can affect several
other operations.

For example, a supplier delay may cause a shortage of raw materials.
That shortage can interrupt production, increase transportation costs,
delay customer orders, and create financial risk.

SupplyChain Sentinel demonstrates how a team of specialized AI agents
can collaborate to investigate these connected problems.

A user can select a crisis type, identify an affected supplier and
shipment, set the severity and estimated delay, and provide additional
details. The application then sends the scenario and available
supply-chain data to a CrewAI workflow. The agents analyze the situation
and produce a consolidated recovery report.

The Streamlit dashboard provides pages for:

-   Monitoring the demo supply-chain data.
-   Creating and launching crisis simulations.
-   Viewing the multi-agent investigation outputs.
-   Reviewing and downloading recovery recommendations.
-   Uploading CSV datasets for analysis.

## 🎯 Problem Statement

Traditional supply-chain crisis response can require teams to gather
information from multiple departments and systems before deciding what
to do. Delays in identifying the relationship between supplier
performance, inventory availability, shipment status, and operational
risk can make a disruption more expensive.

The project explores an AI-assisted approach that organizes this
investigation into specialist tasks and combines their findings into one
recovery strategy.

## 🎯 Objectives

-   Demonstrate a multi-agent AI workflow for supply-chain crisis
    investigation.
-   Separate the investigation into focused specialist responsibilities.
-   Analyze shipment, inventory, and supplier information supplied to
    the application.
-   Identify potential operational and financial consequences of a
    disruption.
-   Generate practical short-term and longer-term recovery
    recommendations.
-   Present the investigation in an accessible Streamlit dashboard.
-   Demonstrate AI workflow execution.

------------------------------------------------------------------------

## ✨ Key Features

### 1. Supply Chain Control Tower

The Overview page presents a high-level view of the available
supply-chain data, including shipment and inventory indicators, charts,
and operational alerts.

### 2. Crisis Simulation

Users can create a disruption scenario by selecting:

-   Crisis type.
-   Affected supplier.
-   Affected shipment.
-   Crisis severity.
-   Estimated delay in days.
-   Additional crisis details.

The submitted scenario is passed to the multi-agent investigation
workflow.

### 3. Six Specialist AI Agents

The application uses six specialist agents. Each agent has a defined
role and contributes to the overall investigation.

### 4. AI-Generated Recovery Report

After the workflow completes, the application displays the final
investigation report. The report can be downloaded as a Markdown file
for review or documentation.

### 5. Agent Execution View

The Agent Execution page displays the configured agents and the task
outputs returned by the CrewAI workflow, where available.

### 6. Recovery Plans

The Recovery Plans page provides access to the generated strategy and
its individual task outputs.

### 7. CSV Data Upload

The Supply Chain Data page allows users to upload CSV datasets. Uploaded
datasets can be used in place of the corresponding demo data during an
investigation. The dashboard also provides a way to clear uploaded
datasets and return to demo data.

------------------------------------------------------------------------

## 🤖 Multi-Agent Architecture

The central idea is to divide a complex supply-chain investigation into
smaller specialist tasks.

The configured agents are:

  -----------------------------------------------------------------------
  Agent                   Role                    Responsibility
  ----------------------- ----------------------- -----------------------
  🚨 Disruption Analyst   Supply Chain Risk       Identifies and
                          Detector                classifies the reported
                                                  disruption and its
                                                  likely impact.

  📦 Inventory Analyst    Inventory Intelligence  Reviews stock levels,
                          Specialist              consumption, inventory
                                                  coverage, and potential
                                                  shortages.

  🏭 Supplier             Supplier Evaluation     Evaluates supplier
  Intelligence            Specialist              information and
                                                  considers possible
                                                  supplier alternatives.

  🚚 Logistics Optimizer  Transportation          Reviews shipment and
                          Optimization Specialist transportation
                                                  constraints and
                                                  considers logistics
                                                  options.

  🛡️ Risk Analyst         Operational Risk        Assesses operational
                          Specialist              and financial exposure
                                                  based on the available
                                                  information.

  🧠 Recovery Coordinator Supply Chain Recovery   Consolidates the
                          Manager                 findings into a
                                                  coordinated recovery
                                                  strategy.
  -----------------------------------------------------------------------

### Workflow

The workflow is designed as a sequential investigation:

``` text
User submits a crisis scenario
              |
              v
      Disruption Analyst
              |
              v
       Inventory Analyst
              |
              v
     Supplier Intelligence
              |
              v
      Logistics Optimizer
              |
              v
         Risk Analyst
              |
              v
      Recovery Coordinator
              |
              v
     Final Recovery Strategy
              |
              v
       Streamlit Dashboard
```

The agents use the shared supply-chain context and the outputs of
earlier tasks to support the later stages of the investigation. The
final coordinator combines the findings into one report.

**Important:** The dashboard's status messages describe the
investigation stages. 

------------------------------------------------------------------------

## 🧰 Technology Stack

  -----------------------------------------------------------------------
  Technology                          Purpose
  ----------------------------------- -----------------------------------
  Python                              Main programming language

  Streamlit                           Interactive web application and
                                      dashboard

  CrewAI                              Multi-agent orchestration

  Google Gemini                       Large language model used by the
                                      agents

  Google Gen AI SDK                   Gemini API integration used by the
                                      project service layer

  Pandas                              Tabular data handling and CSV
                                      processing

  Plotly                              Interactive dashboard charts

  python-dotenv                       Loading configuration and API keys
                                      from `.env`

  LangSmith (optional)                Optional tracing 

  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 📁 Project Structure

The project is organized into separate modules so that the dashboard,
agents, tasks, data, and services can be maintained independently.

A representative structure is:

``` text
SupplyChain-Sentinel/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
├── assets/
│   └── style.css
│
├── data/
│   ├── __init__.py
│   └── demo_data.py
│
├── agents/
│   ├── __init__.py
│   └── supply_chain_agents.py
│
├── tasks/
│   ├── __init__.py
│   └── supply_chain_tasks.py
│
├── crew/
│   ├── __init__.py
│   └── supply_chain_crew.py
│
├── services/
│   ├── gemini_service.py
│   └── crewai_llm.py
│
└── tools/
    └── ...
```

### Main files

-   **`app.py`** --- Streamlit entry point. Builds the dashboard,
    manages session state, accepts crisis scenarios, calls the
    investigation workflow, and displays results.
-   **`config.py`** --- Central application configuration, model
    settings, agent descriptions, navigation items, and configuration
    validation.
-   **`agents/supply_chain_agents.py`** --- Defines the six specialist
    CrewAI agents.
-   **`tasks/supply_chain_tasks.py`** --- Defines the investigation
    tasks and their expected outputs.
-   **`crew/supply_chain_crew.py`** --- Creates the CrewAI crew,
    connects agents and tasks, and exposes the crisis investigation
    function.
-   **`data/demo_data.py`** --- Provides the sample shipment, inventory,
    supplier, and combined demo datasets.
-   **`assets/style.css`** --- Contains the dashboard's custom styling.
-   **`.env`** --- Stores private API keys and local environment
    configuration. This file must not be committed to version control.
-   **`.env.example`** --- Documents the environment variables required
    to configure the project without containing real credentials.

------------------------------------------------------------------------

## ⚙️ How the Application Works

1.  **Application startup:** Streamlit loads the configuration, styles,
    and demo datasets.
2.  **Data selection:** The dashboard uses demo data by default. If a
    user uploads supported CSV datasets, the uploaded data can take
    precedence for the corresponding dataset.
3.  **Scenario creation:** The user selects the crisis details on the
    Crisis Simulation page.
4.  **Workflow initialization:** The application calls
    `run_crisis_investigation()` from `crew/supply_chain_crew.py`.
5.  **Agent creation:** The crew module creates the configured
    specialist agents and their tasks.
6.  **LLM execution:** The agents use the configured Gemini model to
    perform their assigned analysis.
7.  **Task coordination:** The sequential workflow passes relevant task
    context and findings through the investigation.
8.  **Report generation:** The crew returns its final output and, where
    available, individual task outputs.
9.  **Dashboard rendering:** Streamlit stores the results in session
    state and displays the investigation report and agent outputs.
10. **Report export:** The user can download the generated recovery
    report in Markdown format.

The application is an AI-assisted decision-support demonstration. It
does not automatically execute procurement, shipment, payment, or
supplier-management actions.

------------------------------------------------------------------------

## 💻 Installation and Setup

### Prerequisites

Install the following before setting up the project:

-   Python 3.10 or a compatible Python version supported by the
    installed dependencies.
-   pip.
-   A Google AI Studio API key with access to the configured Gemini
    model.
-   A terminal such as PowerShell or the VS Code integrated terminal.

### 1. Clone the repository

If the project is hosted on GitHub:

``` bash
git clone https://github.com/MaryamArif85/Supply-Chain-Agents
cd SupplyChain-Agents
```

### 2. Create a virtual environment

**Windows PowerShell:**

``` powershell
python -m venv venv
```

Activate it:

``` powershell
.\venv\Scripts\Activate.ps1
```

If you use Command Prompt:

``` cmd
venv\Scripts\activate
```

### 3. Upgrade pip

``` bash
python -m pip install --upgrade pip
```

### 4. Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🔐 Environment Configuration

Create a file named `.env` in the root directory of the project.

You can use `.env.example` as a template:

``` dotenv
GOOGLE_API_KEY_1=your_first_google_api_key
GOOGLE_API_KEY_2=your_second_google_api_key
GOOGLE_API_KEY_3=your_third_google_api_key

GEMINI_MODEL=gemini-3.6-flash

LANGSMITH_TRACING=false
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=SupplyChain-Sentinel
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
```

### Environment variable reference

  -----------------------------------------------------------------------
  Variable                            Description
  ----------------------------------- -----------------------------------
  `GOOGLE_API_KEY_1`                  Primary Google Gemini API key.

  `GOOGLE_API_KEY_2`                  Optional additional Google Gemini
                                      API key.

  `GOOGLE_API_KEY_3`                  Optional additional Google Gemini
                                      API key.

  `GEMINI_MODEL`                      Gemini model identifier used by the
                                      project.

  `LANGSMITH_TRACING`                 Enables or disables LangSmith
                                      tracing when the code has been
                                      configured to use it.

  `LANGSMITH_API_KEY`                 LangSmith API key, only needed when
                                      LangSmith tracing is enabled.

  `LANGSMITH_PROJECT`                 Name of the LangSmith project.

  `LANGSMITH_ENDPOINT`                LangSmith API endpoint.
  -----------------------------------------------------------------------

The current CrewAI LLM configuration uses the first configured Google
API key as its primary key. Additional key-handling behavior in the
separate Gemini service does not automatically mean that CrewAI itself
rotates keys.

**Model availability:** The model identifier in `.env` must be available
to the Google account and supported by the installed CrewAI/LLM
integration. If the configured model is unavailable, use a currently
supported Gemini model identifier that your API account can access.

### Keep credentials private

Never paste real API keys into source code, README files, screenshots,
public issue reports, or GitHub commits.

Add the following entries to `.gitignore`:

``` gitignore
.env
venv/
.venv/
__pycache__/
*.py[cod]
.streamlit/secrets.toml
```

------------------------------------------------------------------------

## ▶️ Running the Application

After installing the dependencies and configuring `.env`, run the
application from the project root:

``` bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal, usually:

``` text
http://localhost:8501
```

Open the URL in your browser.

To stop the application, press `Ctrl + C` in the terminal.

------------------------------------------------------------------------

## 🖥️ Using the Dashboard

### 1. Overview

The Overview page provides a summary of the current supply-chain data.
It includes shipment and inventory indicators, visual charts, and
operational alerts based on the loaded dataset.

### 2. Crisis Simulation

1.  Open **Crisis Simulation** from the sidebar.
2.  Choose the type of disruption.
3.  Select the affected supplier.
4.  Select the affected shipment.
5.  Choose the severity.
6.  Enter the estimated delay in days.
7.  Add any additional context that may help the investigation.
8.  Select **Initiate AI Crisis Investigation**.
9.  Wait for the CrewAI workflow to complete.
10. Review the generated investigation report.

The quality of the report depends on the quality and completeness of the
scenario and the supplied data.

### 3. Agent Execution

Open **Agent Execution** to review the specialist agent descriptions and
the task outputs returned by the crew, when those outputs are available.

### 4. Recovery Plans

Open **Recovery Plans** to review the final recovery strategy and
supporting task outputs. Use the download option to save the report.

### 5. Supply Chain Data

Open **Supply Chain Data** to inspect the available datasets and upload
CSV files. Uploaded data is held in the Streamlit session while the
application is running. Use the page's clear-upload option to return to
the demo datasets.

------------------------------------------------------------------------

## 📊 Supply-Chain Data

The application includes demo datasets for:

-   Shipments.
-   Inventory.
-   Suppliers.

These datasets allow the dashboard and crisis simulation to be
demonstrated without connecting to a live enterprise resource-planning
or supply-chain management system.

### Using your own CSV files

The Supply Chain Data page provides CSV upload controls. For best
results:

-   Upload the appropriate dataset to its matching data category.
-   Use clear, consistent column names.
-   Keep identifiers consistent across related datasets. For example,
    supplier IDs in shipment records should correspond to supplier IDs
    in the supplier dataset.
-   Use numeric values for quantities, stock levels, delays, and costs
    where appropriate.
-   Avoid blank or inconsistent identifiers.
-   Check that date fields use a consistent format.

The exact column names expected by the current application are
determined by the data-handling code and demo dataset schema. If you
plan to use a different CSV schema, update the relevant data-processing
logic before running an investigation.

**Data note:** Uploaded CSV data is not automatically verified against a
real supply-chain system. The application should not be assumed to
validate every business rule or data relationship.

------------------------------------------------------------------------

## 🔎 AI Tracing and Observability

Tracing helps developers understand how an AI workflow executes, which
tasks run, and where errors or delays may occur.

### CrewAI tracing

The project has demonstrated CrewAI's own tracing/export mechanism. A
successful run may display a message indicating that spans have been
exported and may provide a trace link.

CrewAI tracing is distinct from LangSmith. A CrewAI trace link should
not be described as a LangSmith trace.

### Optional LangSmith configuration

The configuration includes LangSmith-related environment variables.
Setting `LANGSMITH_TRACING=true` 

------------------------------------------------------------------------

## 🧪 Example Crisis Scenario

The following is an illustrative scenario based on the type of demo data
used during development. Values should be checked against the current
dataset before treating them as authoritative.

**Scenario:** A shipment of industrial resin is delayed, creating a
possible raw-material shortage.

Example inputs:

  Field                        Example value
  ---------------------------- ----------------------
  Crisis type                  Shipment Delay
  Shipment                     `SHP-1001`
  Supplier                     Global Raw Materials
  Product                      Industrial Resin
  Severity                     High
  Estimated additional delay   5 days

The investigation may consider:

-   The reported shipment delay and its uncertainty.
-   Current inventory and average daily consumption.
-   Estimated inventory coverage.
-   Supplier reliability information available in the dataset.
-   Possible logistics alternatives.
-   Operational and financial exposure.
-   Short-term actions to reduce disruption.
-   Longer-term actions to improve supply-chain resilience.

Potential recommendations might include reviewing consumption
priorities, requesting supplier updates, evaluating alternative
sourcing, considering expedited transportation, or revisiting
safety-stock policies.

These are examples of analysis topics, not guaranteed recommendations or
confirmed real-world actions. The AI should distinguish dataset facts
from assumptions and should not invent supplier approvals, available
stock, transport capacity, prices, or confirmed delivery dates.

------------------------------------------------------------------------

## 🛠️ Troubleshooting

### 1. `ModuleNotFoundError`

**Possible cause:** Dependencies were installed into a different Python
environment, or the virtual environment is not active.

**Try:**

``` bash
.\venv\Scripts\activate
pip install -r requirements.txt
```

Run Streamlit from the project root so Python can resolve the project
packages.

### 2. Missing Google API key

**Possible cause:** `.env` is missing, the variable name is incorrect,
or the environment file is not being loaded.

**Check:**

-   The file is named `.env`.
-   It is in the project root.
-   At least `GOOGLE_API_KEY_1` contains a valid key.
-   The key has not been revoked or restricted in a way that blocks the
    request.

Restart Streamlit after changing environment variables.

### 3. Gemini model not found or unavailable

**Possible cause:** The configured model identifier is not available to
the API key, or the provider does not currently expose it.

**Try:** Check the model availability in Google AI Studio and set
`GEMINI_MODEL` to an available model supported by the installed
integration.

### 4. API quota, rate-limit, or server errors

**Possible cause:** The API project has reached a quota, the service is
temporarily unavailable, or the selected model is experiencing an issue.

**Try:**

-   Check the Google AI Studio project and quota.
-   Confirm that the API key belongs to the intended project.
-   Wait and retry if the provider reports a temporary service error.
-   Avoid repeatedly submitting the same long-running investigation.

### 5. CrewAI LLM configuration error

**Possible cause:** The model name, provider prefix, API key, or
installed package versions are incompatible.

**Check:** The CrewAI LLM configuration in `services/crewai_llm.py`,
especially the model identifier and API key passed to `crewai.LLM`.

### 6. CSV upload or column error

**Possible cause:** The uploaded file does not contain columns expected
by the dashboard or agent context.

**Try:**

-   Compare the CSV headers with the demo dataset columns.
-   Check for missing identifiers and numeric fields.
-   Upload a clean CSV with consistent column names.
-   Update the data-processing code if your schema is different.

### 7. Streamlit indentation or syntax error

**Possible cause:** A code block was pasted at the wrong indentation
level or a function block was not closed correctly.

**Try:**

-   Check the line number in the traceback.
-   Confirm that page-specific logic is inside its corresponding
    `render_...()` function.
-   Remove duplicated old blocks after replacing a section.
-   Save the file and restart Streamlit.

### 8. Investigation fails but the dashboard loads

**Possible cause:** The UI is working, but the CrewAI workflow or LLM
request failed.

**Check:** The terminal traceback and the investigation error displayed
in the Crisis Simulation page. The dashboard and the AI workflow are
separate parts of the application, so a successful page load does not
guarantee a successful model call.

------------------------------------------------------------------------
Check live app  https://supply-chain-agents-wfseyc8l6rfyevmmgrp8bn.streamlit.app/
------------------------------------------------------------------------

## 🚧 Limitations and Future Improvements

SupplyChain Sentinel is a demonstration application. The following
enhancements could make it more robust:

-   Connect to live ERP, warehouse, procurement, and transportation
    systems.
-   Add data validation and schema mapping for uploaded CSV files.
-   Add automated anomaly detection for shipment and inventory data.
-   Improve the calculation and verification of inventory coverage,
    reorder points, and shortage dates.
-   Require agents to cite the exact dataset fields supporting
    quantitative claims.
-   Clearly label assumptions, estimates, and unverified supplier
    alternatives.
-   Add human approval steps before a recovery recommendation is treated
    as an operational decision.
-   Add real-time progress callbacks for individual agent execution.
-   Add richer LangSmith integration if centralized tracing is required.
-   Add persistent storage for investigation history and uploaded
    datasets.
-   Add user authentication and role-based access.
-   Add scenario comparison and recovery-plan evaluation.
-   Add export options such as PDF and Excel.

------------------------------------------------------------------------

## 🤝 Contributing

Contributions and suggestions are welcome.

A typical contribution workflow:

1.  Fork the repository.
2.  Create a feature branch.
3.  Make your changes.
4.  Test the application locally.
5.  Submit a pull request describing the changes.

When reporting a problem, include the relevant error message and steps
to reproduce it. Never include API keys or private business data in an
issue.

------------------------------------------------------------------------

## 👩‍💻 Project Summary

**SupplyChain Sentinel** demonstrates how a coordinated team of AI
agents can assist with supply-chain disruption analysis and recovery
planning.

By combining CrewAI orchestration, Google Gemini, Python data
processing, and a Streamlit control-tower interface, the project
provides an educational example of multi-agent AI applied to operational
decision support.

**Built with Python, Streamlit, CrewAI, and Google Gemini.**
