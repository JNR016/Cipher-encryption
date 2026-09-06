# File Encryption (v2.0.0)

A secure command-line tool written in Python that protects files using authenticated **AES-128 encryption**. 

This application is an upgrade from legacy Version 1.0.0 character-shift cipher. By processing files as binary data (`rb`/`wb`) and leveraging the industry-standard **Fernet (cryptography)** framework, the tool securely encrypts and decrypts text documents, multimedia images, audio tracks, and PDFs without risking data corruption.

## Key Features

- **Authenticated AES-128 Encryption:** Uses the secure Fernet blueprint, combining AES encryption in CBC mode with HMAC authentication to prevent file tampering.
- **Expanded File Support:** Securely processes `.txt`, `.json`, `.csv`, `.py`, `.html`, `.png`, `.jpg`, `.jpeg`, `.gif`, `.mp3`, `.wav`, `.docx`, and `.pdf` files.
- **Hidden Key Input:** Leverages secure terminal inputs to mask your decryption key as you type, keeping it hidden from shoulder-surfers.
- **Dynamic File Preservation:** Intelligently extracts the original file's extension to automatically format timestamped outputs.
- **Non-Destructive Operations:** Writes data strictly to brand-new files, leaving your source assets completely untouched.

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.x
- The `cryptography` third-party library.

### Installation
Install the official cryptographic dependency via your terminal:
```bash
pip install cryptography
```

### How to Run
Run the script by passing the target file path directly as a command-line argument:
```bash
python secure_encryptor.py path/to/your/file.png
```

---

## CLI User Interface Walkthrough

### 1. Encryption Mode (`e`)
When encrypting, the script automatically handles key generation and displays your secret key. **You must save this key** to open the file later.

```text
Which mode would you like to do.
To encrypt a file enter 'e' and to decrypt a file enter 'd': e
Generating a key...
The generated key is: gAAAAABm...[Your Secret Key String]...
Please save the key as it is required to decrypt the file!!!
File encrypted successfully.🔒

Do you want to name the file or use the default naming (decryptedData_time.png)
(Enter 'yes' for new name or 'no' for default): no
```
*Output generated:* `encryptedData_2026-09-06_22-45-00.png`

### 2. Decryption Mode (`d`)
When decrypting, your typing is safely hidden from view. If the key is wrong or the file is modified, the system safely triggers a security rejection.

```text
Which mode would you like to do.
To encrypt a file enter 'e' and to decrypt a file enter 'd': d
Enter a key to decrypt the file: ********************************************
File decrypted successfully.🔓
```

---

## ⚠️ Compatibility & Portfolio Note

- **Breaking Changes:** Version 2.0.0 is a complete cryptographic rebuild. It is **not backwards-compatible** with files encrypted using the Version 1.0.0 shift cipher.
- **Looking for V1?** If you need to access the legacy character-shift cipher code or documentation designed for simple `.txt` operations, please refer directly to the [v1.0.0 Source Code Release](https://github.com/JNR016/Cipher-encryption/releases/tag/v1.0.0).

---

## 📈 Evolution History

### [v2.0.0] - Current Release
- **Added:** Integrated `cryptography.fernet` for robust authenticated AES-128 operations.
- **Added:** Secure hidden password inputs via the native `getpass` module.
- **Added:** Broad support for multimedia and document extensions (`.png`, `.pdf`, `.docx`, etc.).
- **Removed:** Legacy character substitution loops.

### [v1.0.0] - Legacy Release
- Initial proof-of-concept custom character-shift cipher.
- Text-only restriction (`.txt`, `.json`, `.csv`, `.py`, `.html`).

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
