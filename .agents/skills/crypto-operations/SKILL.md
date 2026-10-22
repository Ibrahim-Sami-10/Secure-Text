---
name: crypto-operations
description: >-
  Use this skill when implementing, testing, debugging, or verifying cryptographic algorithms
  (Caesar Cipher, AES-256-CBC, RSA-2048 OAEP, SHA-256) or when modifying encryption/decryption
  helpers in SecureText.
---

# Cryptographic Operations Skill

This skill documents the cryptographic standards, encoding conventions, and verification
procedures implemented in SecureText.

## Algorithm Specifications

| Algorithm | Type | Implementation | Padding / Encoding | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Caesar** | Classical | Custom shift of 3 | Preserves casing & symbols | Reversible |
| **AES-256** | Symmetric | `Crypto.Cipher.AES` (CBC mode) | PKCS#7 (`AES.block_size` = 16) | IV (16B) + Ciphertext combined, Base64 |
| **RSA-2048** | Asymmetric | `Crypto.PublicKey.RSA` + `PKCS1_OAEP` | OAEP Padding | Returns Base64 ciphertext & PEM private key |
| **SHA-256** | Hash | Python standard `hashlib.sha256` | 256-bit Hex digest (64 chars) | One-way irreversible |

## Encoding Conventions

1. **AES-CBC Ciphertext Structure:**
   - IV generation: `get_random_bytes(16)`
   - Combined payload: `iv + encrypted_data`
   - Encoded as Base64 string for transport.
   - During decryption: First 16 bytes extracted as IV, remainder as ciphertext.
2. **AES Key:**
   - 256-bit (32 bytes) random bytes, Base64 encoded.
3. **RSA Key Pair:**
   - 2048-bit key generated on the fly.
   - Private key exported in standard PEM format.

## Verification Procedure

Always run the automated verification script after making changes to cryptographic logic:

```bash
python .agents/skills/crypto-operations/scripts/verify_crypto.py
```

Expected output:
- All 4 suites report `[OK]`
- Exit code 0
