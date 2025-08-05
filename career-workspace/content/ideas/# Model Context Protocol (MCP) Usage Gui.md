# Model Context Protocol (MCP) Usage Guide

This guide provides a thorough explanation of how MCP tools can be used in both **interactive agent sessions** (e.g. Cursor) and **automation workflows**.

---

## 🔹 What is MCP?

MCP (Model Context Protocol) is a standardized way for tools to expose capabilities (like fetching ad data or updating spreadsheets) via CLI or HTTP. These tools can be used directly by AI agents (e.g. in Cursor) or in scripts and automation pipelines.

---

## 🧠 Using MCP in Cursor Sessions (Interactive Agent Use)

Once you’ve connected an MCP server to your Cursor config (e.g. Google Ads, Meta Ads, Airtable), you can ask the agent to use it with natural language:

### Example:
> “Show me last week’s Meta campaign spend and ROAS.”

The agent will:
- Detect intent
- Call the correct MCP tool
- Format and display the results
- Optionally generate visualizations or export data

### Popular MCP Integrations:
- `mcp-google-ads`: list campaigns, run GAQL queries, fetch spend and ROAS
- `meta-ads-mcp`: analyze Facebook/Instagram campaigns
- `airtable-mcp` or `google-sheets-mcp`: write and read from tabular storage

These tools work seamlessly once added to `.cursor/mcp.json`.

---

## ⚙️ Using MCP in Automation Workflows (No Agent Required)

You can run the exact same MCP tools in cron jobs, scripts, CI/CD workflows, or schedulers without needing any agent UI.

### Example: Bash Script with Cron
```bash
#!/bin/bash

# Fetch last 24h campaign performance
mcp-google-ads list_campaigns --since=1d > daily_report.json

# Parse and insert into Airtable
jq '.campaigns[] | {name, cpa}' daily_report.json | \
npx @felores/airtable-mcp createRecord \
  --base "AdReports" \
  --table "Google Daily"
```

### Example: Python
```python
import subprocess, json

output = subprocess.check_output(
  ["mcp-google-ads", "list_campaigns", "--since=7d"]
)
data = json.loads(output)
# Do something with `data`
```

### Automation Platforms:
- **cron-mcp**: Run MCP tasks on a schedule
- **n8n/Make**: Use CLI-based MCPs in multi-step automations
- **Airflow/GitHub Actions**: Integrate into pipelines

---

## ✅ Summary

| Use Case | Agent in Cursor | Automation Workflow |
|----------|------------------|----------------------|
| Fetch Google/Meta ad data | ✅ Natural language | ✅ Script/cron/CI |
| Write to Sheets or Airtable | ✅ Prompt-based | ✅ CLI/API call |
| Schedule regular reports | 🟡 Via `cron-mcp` | ✅ Native cron/Airflow/etc. |

---

With MCP, your data tools become accessible in both human-friendly sessions and machine-friendly automations — creating a unified system of interaction across use cases.
