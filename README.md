# SecureText

[![Live Demo](https://img.shields.io/badge/Live%20Demo-secure--text--tool.vercel.app-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://secure-text-tool.vercel.app)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)
![PyCryptodome](https://img.shields.io/badge/Crypto-PyCryptodome-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Deployment](https://img.shields.io/badge/Deployment-Vercel-black?logo=vercel)

**SecureText** is a lightweight web-based cryptography application for experimenting with classical encryption, symmetric encryption, asymmetric encryption, and one-way hashing.

Built with **Python (Flask)**, **JavaScript (ES6)**, and **PyCryptodome**.

> **Educational use only:** This project is intended for learning and experimentation and should not be used to protect production data or real secrets.

🌐 **Live Demo:** [https://secure-text-tool.vercel.app](https://secure-text-tool.vercel.app)

## 🎥 Preview

https://github.com/user-attachments/assets/b97bf082-b736-469d-b846-40ced0a17ce5


## 🚀 Features

- **Caesar Cipher:** Classical substitution with fixed shift
- **AES-256-CBC:** High-grade symmetric encryption with random IV & key generation
- **RSA-2048:** Public-key asymmetric encryption with PKCS1_OAEP padding
- **SHA-256:** Cryptographic one-way hashing
- **Security Hardening:** Payload size limits (1MB max), strict type checks, and HTTP security headers (CSP, nosniff, frame protection)
- **Interactive UI:** Real-time key generation, copy-to-clipboard, error toasts, and dark cybersecurity styling

## 🔐 Supported Algorithms

| Algorithm         | Category              | Specification        | Reversible? | Max Payload |
| ----------------- | --------------------- | -------------------- | :---------: | :---------: |
| **Caesar Cipher** | Classical             | Fixed shift of 3     |     ✅      | Arbitrary   |
| **AES-256**       | Symmetric Encryption  | CBC + PKCS#7 Padding |     ✅      | 1 MB        |
| **RSA-2048**      | Asymmetric Encryption | OAEP Padding         |     ✅      | ~214 bytes  |
| **SHA-256**       | Cryptographic Hash    | 256-bit Digest       |     ❌      | 1 MB        |

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, Flask
- **Cryptography:** PyCryptodome, `hashlib`, `base64`
- **Frontend:** HTML5, CSS3 (Custom Dark Theme), JavaScript (ES6 Fetch API)
- **Deployment:** Vercel (Serverless Python), Gunicorn WSGI compatible

## 📂 Project Structure

```text
Secure-Text/
├── app.py              # Main Flask application & cryptographic routes
├── index.py            # Deployment entrypoint alias
├── requirements.txt    # Project dependencies
├── Procfile            # Optional traditional WSGI declaration (Gunicorn)
├── README.md           # Documentation & instructions
├── static/
│   ├── script.js       # Frontend interaction & asynchronous API handler
│   └── style.css       # Cybersecurity theme stylesheet
└── templates/
    └── index.html      # Responsive web interface
```

## ⚙️ Installation & Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Ibrahim-Sami-10/Secure-Text.git
cd Secure-Text
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the application

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

## ☁️ Deployment (Vercel)

This project is built to deploy seamlessly on **Vercel** with zero manual server configuration:

1. Import the repository in [Vercel](https://vercel.com).
2. Framework Preset will automatically detect **Flask**.
3. Every push to the `main` branch automatically deploys to [https://secure-text-tool.vercel.app](https://secure-text-tool.vercel.app).

## 🔒 Security & Implementation Notes

- **Caesar Cipher:** Classical educational cipher; provides no modern cryptographic defense.
- **AES-CBC:** Uses CBC mode with a unique random IV prepended to the ciphertext. Production systems handling sensitive data should typically use authenticated encryption (e.g. AES-GCM).
- **RSA-2048:** Generates ephemeral 2048-bit key pairs with PKCS1_OAEP padding. Due to OAEP mathematical padding overhead, plaintext is limited to ~214 bytes per encryption.
- **SHA-256:** Cryptographic hash function producing a 64-character hexadecimal digest. Hashes cannot be decrypted.
- **DoS Protection & Headers:** The app enforces a 1 MB payload cap and serves `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, and `X-Frame-Options: DENY` headers.

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

