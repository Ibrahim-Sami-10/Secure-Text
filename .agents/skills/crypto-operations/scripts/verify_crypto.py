"""
Automated Cryptography Verification Script for SecureText.
Tests all algorithms (Caesar, AES-256-CBC, RSA-2048, SHA-256) for both
encryption and decryption consistency.
"""

import sys
import os

# Add root directory to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from app import (
    caesar_encrypt, caesar_decrypt,
    aes_encrypt, aes_decrypt,
    rsa_encrypt, rsa_decrypt,
    sha256_hash,
)

def run_tests():
    sample_text = "SecureText: The quick brown fox jumps over 123 lazy dogs!"
    print(f"Testing with sample: '{sample_text}'\n")

    # 1. Caesar Cipher
    print("[1/4] Testing Caesar Cipher...")
    c_cipher = caesar_encrypt(sample_text, 3)
    c_plain = caesar_decrypt(c_cipher, 3)
    assert c_plain == sample_text, f"Caesar mismatch: expected '{sample_text}', got '{c_plain}'"
    print("  [OK] Caesar Cipher passed.")

    # 2. AES-256-CBC
    print("[2/4] Testing AES-256-CBC...")
    aes_cipher, aes_key = aes_encrypt(sample_text)
    aes_plain = aes_decrypt(aes_cipher, aes_key)
    assert aes_plain == sample_text, f"AES mismatch: expected '{sample_text}', got '{aes_plain}'"
    print("  [OK] AES-256-CBC passed.")

    # 3. RSA-2048 OAEP
    print("[3/4] Testing RSA-2048 PKCS1_OAEP...")
    rsa_cipher, rsa_private_key = rsa_encrypt(sample_text)
    rsa_plain = rsa_decrypt(rsa_cipher, rsa_private_key)
    assert rsa_plain == sample_text, f"RSA mismatch: expected '{sample_text}', got '{rsa_plain}'"
    print("  [OK] RSA-2048 passed.")

    # 4. SHA-256
    print("[4/4] Testing SHA-256 Hash...")
    hash1 = sha256_hash(sample_text)
    hash2 = sha256_hash(sample_text)
    assert hash1 == hash2, "SHA-256 hash inconsistency"
    assert len(hash1) == 64, f"SHA-256 hex length should be 64, got {len(hash1)}"
    print("  [OK] SHA-256 passed.")

    print("\nAll 4 cryptographic suites passed verification successfully!")

if __name__ == "__main__":
    run_tests()
