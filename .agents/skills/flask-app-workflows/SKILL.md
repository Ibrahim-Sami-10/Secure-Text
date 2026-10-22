---
name: flask-app-workflows
description: >-
  Use this skill when developing locally, adding or modifying Flask routes, updating frontend
  templates/CSS/JavaScript, or testing API contracts in SecureText.
---

# Flask Application Workflows Skill

This skill documents local development, API request/response contracts, and frontend
integration patterns for SecureText.

## Local Development Server

Run the development server locally:
```bash
python app.py
```
App runs at `http://127.0.0.1:5000` with hot-reloading enabled in debug mode.

## API Endpoints

### 1. `POST /encrypt`
**Request Payload:**
```json
{
  "text": "Hello World",
  "algorithm": "caesar" | "aes" | "rsa" | "sha256"
}
```
**Response (200 OK):**
- Caesar / SHA-256: `{"ciphertext": "..."}`
- AES / RSA: `{"ciphertext": "...", "key": "..."}`
**Error (400 Bad Request):**
- `{"error": "Please enter some text."}` or `{"error": "Please select an algorithm."}`

### 2. `POST /decrypt`
**Request Payload:**
```json
{
  "ciphertext": "...",
  "algorithm": "caesar" | "aes" | "rsa",
  "key": "..." // Required for AES and RSA
}
```
**Response (200 OK):**
- `{"plaintext": "..."}`
**Error Handling:**
- SHA-256 requests return 400: `"SHA-256 is a one-way hash and cannot be decrypted."`
- Malformed inputs or incorrect keys return 400 with descriptive error.

## Frontend Assets

- **Templates:** [templates/index.html](file:///c:/Users/Home/Encryption-Tool/templates/index.html)
- **Styles:** [static/style.css](file:///c:/Users/Home/Encryption-Tool/static/style.css) (dark cybersecurity theme)
- **Logic:** [static/script.js](file:///c:/Users/Home/Encryption-Tool/static/script.js) (asynchronous `fetch` calls to `/encrypt` and `/decrypt`)
