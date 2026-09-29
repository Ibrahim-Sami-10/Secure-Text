import hashlib
import base64

from flask import Flask, render_template, request, jsonify
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad

app = Flask(__name__)


# -------------------------
# Caesar Cipher
# -------------------------

def caesar_encrypt(text, shift):
    result = ""

    for character in text:
        if character.isupper():
            result += chr((ord(character) - ord("A") + shift) % 26 + ord("A"))
        elif character.islower():
            result += chr((ord(character) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += character

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# -------------------------
# AES-256-CBC
# -------------------------

def aes_encrypt(text):
    key = get_random_bytes(32)
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(text.encode("utf-8"), AES.block_size))

    # Store IV with ciphertext so it can be recovered during decryption.
    combined = iv + encrypted_data

    return (
        base64.b64encode(combined).decode("utf-8"),
        base64.b64encode(key).decode("utf-8")
    )


def aes_decrypt(ciphertext, key_text):
    key = base64.b64decode(key_text)
    combined = base64.b64decode(ciphertext)

    if len(combined) < 32:
        raise ValueError("Invalid AES ciphertext.")

    iv = combined[:16]
    encrypted_data = combined[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    return decrypted_data.decode("utf-8")


# -------------------------
# RSA-2048
# -------------------------

def rsa_encrypt(text):
    key = RSA.generate(2048)
    public_key = key.publickey()

    cipher = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher.encrypt(text.encode("utf-8"))

    return (
        base64.b64encode(encrypted_data).decode("utf-8"),
        key.export_key().decode("utf-8")
    )


def rsa_decrypt(ciphertext, private_key_text):
    private_key = RSA.import_key(private_key_text)

    cipher = PKCS1_OAEP.new(private_key)
    encrypted_data = base64.b64decode(ciphertext)

    return cipher.decrypt(encrypted_data).decode("utf-8")


# -------------------------
# SHA-256
# -------------------------

def sha256_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# -------------------------
# Pages
# -------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# Encryption / Hashing
# -------------------------

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json() or {}

    text = data.get("text", "")
    algorithm = data.get("algorithm", "")

    if not text.strip():
        return jsonify({"error": "Please enter some text."}), 400

    if not algorithm:
        return jsonify({"error": "Please select an algorithm."}), 400

    try:
        if algorithm == "caesar":
            return jsonify({
                "ciphertext": caesar_encrypt(text, 3)
            })

        if algorithm == "aes":
            ciphertext, key = aes_encrypt(text)
            return jsonify({
                "ciphertext": ciphertext,
                "key": key
            })

        if algorithm == "rsa":
            ciphertext, private_key = rsa_encrypt(text)
            return jsonify({
                "ciphertext": ciphertext,
                "key": private_key
            })

        if algorithm == "sha256":
            return jsonify({
                "ciphertext": sha256_hash(text)
            })

        return jsonify({"error": "Invalid algorithm."}), 400

    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    except Exception:
        return jsonify({"error": "Encryption failed. Please try again."}), 500


# -------------------------
# Decryption
# -------------------------

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json() or {}

    ciphertext = data.get("ciphertext", "")
    algorithm = data.get("algorithm", "")
    key = data.get("key", "")

    if not ciphertext.strip():
        return jsonify({"error": "Please enter ciphertext."}), 400

    if not algorithm:
        return jsonify({"error": "Please select an algorithm."}), 400

    if algorithm == "sha256":
        return jsonify({
            "error": "SHA-256 is a one-way hash and cannot be decrypted."
        }), 400

    try:
        if algorithm == "caesar":
            return jsonify({
                "plaintext": caesar_decrypt(ciphertext, 3)
            })

        if algorithm == "aes":
            if not key.strip():
                return jsonify({"error": "AES key is required."}), 400

            return jsonify({
                "plaintext": aes_decrypt(ciphertext, key.strip())
            })

        if algorithm == "rsa":
            if not key.strip():
                return jsonify({"error": "RSA private key is required."}), 400

            return jsonify({
                "plaintext": rsa_decrypt(ciphertext, key.strip())
            })

        return jsonify({"error": "Invalid algorithm."}), 400

    except Exception:
        return jsonify({
            "error": "Decryption failed. Check the ciphertext and key."
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
