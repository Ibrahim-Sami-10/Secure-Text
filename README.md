# SecureText

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)
![PyCryptodome](https://img.shields.io/badge/Crypto-PyCryptodome-red.svg)

**SecureText** is a lightweight web-based cryptography application for experimenting with classical encryption, symmetric encryption, asymmetric encryption, and one-way hashing.

Built with **Python (Flask)**, **JavaScript (ES6)**, and **PyCryptodome**.

> **Educational use only:** This project is intended for learning and experimentation and should not be used to protect production data or real secrets.

## 🚀 Features

- Caesar Cipher encryption and decryption
- AES-256-CBC encryption and decryption
- RSA-2048 encryption and decryption
- SHA-256 cryptographic hashing
- Input validation and error handling
- Copy results to clipboard
- Clear workspace
- Responsive cybersecurity-themed interface

## 🔐 Supported Algorithms

| Algorithm         | Category              | Specification        | Reversible? |
| ----------------- | --------------------- | -------------------- | :---------: |
| **Caesar Cipher** | Classical             | Fixed shift of 3     |     ✅      |
| **AES-256**       | Symmetric Encryption  | CBC + PKCS#7 Padding |     ✅      |
| **RSA-2048**      | Asymmetric Encryption | OAEP Padding         |     ✅      |
| **SHA-256**       | Cryptographic Hash    | 256-bit Digest       |     ❌      |

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Cryptography:** PyCryptodome, `hashlib`
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

## 📂 Project Structure

```text
Encryption-Tool/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   ├── script.js
│   └── style.css
└── templates/
    └── index.html
```

## ⚙️ Installation & Run

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

## 🔒 Security Notes

- **Caesar Cipher:** Educational only; provides no meaningful modern security.
- **AES-CBC:** Uses CBC mode without authentication. Production applications should use an authenticated mode such as AES-GCM.
- **RSA:** Generates a new 2048-bit key pair for each encryption operation and uses OAEP padding.
- **AES:** Generates a new key and IV for each encryption operation.
- **SHA-256:** A one-way cryptographic hash and cannot be decrypted.

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of this software, subject to the terms of the MIT License.

See the `LICENSE` file for the full license text.
