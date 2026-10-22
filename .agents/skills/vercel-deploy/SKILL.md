---
name: vercel-deploy
description: >-
  Use this skill when deploying, inspecting, diagnosing, or managing Vercel deployments,
  production domains, and serverless Flask architecture for SecureText.
---

# Vercel Deployment Skill

This skill documents how SecureText is deployed and maintained on Vercel using the official
Flask Framework-Defined Infrastructure (FDI).

## Production Details

- **Project ID:** `prj_FFMwAmay1qXKVczVE1QTDHw6WqNZ`
- **Project Name:** `secure-text`
- **Assigned Live Domain:** [https://secure-text-tool.vercel.app](https://secure-text-tool.vercel.app)
- **Framework Preset:** `flask` (Zero-Configuration)

## Architectural Guidelines

1. **Root-Level Architecture:**
   - [app.py](file:///c:/Users/Home/Encryption-Tool/app.py) contains the main Flask application instance (`app`).
   - [index.py](file:///c:/Users/Home/Encryption-Tool/index.py) provides the entrypoint alias (`from app import app`).
   - [templates/](file:///c:/Users/Home/Encryption-Tool/templates/) and [static/](file:///c:/Users/Home/Encryption-Tool/static/) live at project root.
   - Do **NOT** add a `vercel.json` with manual `/api` rewrites or `includeFiles` arrays; Vercel's Flask preset automatically bundles and routes the full application.

2. **Inspecting Deployments via Vercel MCP:**
   - Use `list_deployments` with `projectId: "prj_FFMwAmay1qXKVczVE1QTDHw6WqNZ"` to check build states (`READY`, `BUILDING`, `ERROR`).
   - Use `get_deployment` with deployment ID to view error logs or target URLs.
   - Use `list_project_domains` to inspect assigned custom domains and verification status.

3. **Deploy Workflow:**
   - Every push to `main` on `https://github.com/Ibrahim-Sami-10/Secure-Text.git` automatically triggers an optimized Vercel build.
