const algorithm = document.getElementById("algorithm");
const plainText = document.getElementById("plainText");
const cipherText = document.getElementById("cipherText");
const keyField = document.getElementById("key");
const decryptedText = document.getElementById("decryptedText");

const encryptButton = document.getElementById("encryptButton");
const decryptButton = document.getElementById("decryptButton");
const copyButton = document.getElementById("copyButton");
const clearButton = document.getElementById("clearButton");

const keySection = document.getElementById("keySection");
const algorithmInfo = document.getElementById("algorithmInfo");
const resultType = document.getElementById("resultType");
const toast = document.getElementById("toast");

const algorithmDescriptions = {
    caesar: "Shifts each letter by 3 positions. Numbers, spaces and symbols stay unchanged.",
    aes: "AES-256-CBC is symmetric encryption. A random 256-bit key is generated for each message.",
    rsa: "RSA-2048 uses asymmetric encryption. A new RSA key pair is generated for each message.",
    sha256: "SHA-256 creates a fixed 256-bit one-way hash. It is hashing, not encryption."
};


function showToast(message) {
    toast.textContent = message;
    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 2200);
}


function updateInterface() {
    const selected = algorithm.value;

    if (!selected) {
        algorithmInfo.textContent =
            "Select an algorithm to see what it does.";
        keySection.style.display = "block";
        decryptButton.style.display = "flex";
        resultType.textContent = "OUTPUT";
        return;
    }

    algorithmInfo.textContent = algorithmDescriptions[selected];

    if (selected === "sha256") {
        keySection.style.display = "none";
        decryptButton.style.display = "none";
        resultType.textContent = "HASH";
    } else if (selected === "caesar") {
        keySection.style.display = "none";
        decryptButton.style.display = "flex";
        resultType.textContent = "CIPHERTEXT";
    } else {
        keySection.style.display = "block";
        decryptButton.style.display = "flex";
        resultType.textContent = "CIPHERTEXT";
    }
}


algorithm.addEventListener("change", updateInterface);


encryptButton.addEventListener("click", async function () {

    const text = plainText.value;
    const selectedAlgorithm = algorithm.value;

    if (!text.trim()) {
        showToast("Please enter some text.");
        plainText.focus();
        return;
    }

    if (!selectedAlgorithm) {
        showToast("Please select an algorithm.");
        algorithm.focus();
        return;
    }

    encryptButton.disabled = true;
    encryptButton.querySelector("span").textContent = "Processing...";

    try {
        const response = await fetch("/encrypt", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text,
                algorithm: selectedAlgorithm
            })
        });

        const data = await response.json();

        if (!response.ok || data.error) {
            showToast(data.error || "Something went wrong.");
            return;
        }

        cipherText.value = data.ciphertext;

        keyField.value = data.key || "";

        decryptedText.value = "";

        if (selectedAlgorithm === "sha256") {
            showToast("SHA-256 hash generated.");
        } else {
            showToast("Encryption completed.");
        }

    } catch (error) {
        showToast("Could not connect to the server.");
    } finally {
        encryptButton.disabled = false;
        encryptButton.querySelector("span").textContent = "Encrypt / Hash";
    }
});


decryptButton.addEventListener("click", async function () {

    const ciphertext = cipherText.value;
    const selectedAlgorithm = algorithm.value;
    const key = keyField.value;

    if (!ciphertext.trim()) {
        showToast("Please enter ciphertext.");
        cipherText.focus();
        return;
    }

    if (!selectedAlgorithm) {
        showToast("Please select an algorithm.");
        algorithm.focus();
        return;
    }

    if (selectedAlgorithm === "sha256") {
        showToast("SHA-256 cannot be decrypted.");
        return;
    }

    if ((selectedAlgorithm === "aes" || selectedAlgorithm === "rsa") &&
        !key.trim()) {
        showToast("A decryption key is required.");
        keyField.focus();
        return;
    }

    decryptButton.disabled = true;

    try {
        const response = await fetch("/decrypt", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                ciphertext: ciphertext,
                algorithm: selectedAlgorithm,
                key: key
            })
        });

        const data = await response.json();

        if (!response.ok || data.error) {
            showToast(data.error || "Decryption failed.");
            return;
        }

        decryptedText.value = data.plaintext;
        showToast("Decryption completed.");

    } catch (error) {
        showToast("Could not connect to the server.");
    } finally {
        decryptButton.disabled = false;
    }
});


copyButton.addEventListener("click", async function () {

    if (!cipherText.value) {
        showToast("There is no result to copy.");
        return;
    }

    try {
        await navigator.clipboard.writeText(cipherText.value);
        showToast("Result copied to clipboard.");
    } catch (error) {
        showToast("Copy failed. Please copy it manually.");
    }
});


clearButton.addEventListener("click", function () {
    plainText.value = "";
    cipherText.value = "";
    keyField.value = "";
    decryptedText.value = "";

    showToast("Workspace cleared.");
});


updateInterface();
