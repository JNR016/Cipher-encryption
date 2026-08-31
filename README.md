# Cipher Encryption

A simple Python script that encrypts or decrypts text files using a custom character-shift cipher.

## What it does

The script reads a text-based file, applies a key-based transformation to each character, and saves the result to a new file.

It supports the following file types:

- .txt
- .json
- .csv
- .py
- .html

The cipher alphabet includes:

- space
- punctuation
- digits
- uppercase letters
- lowercase letters

This means each character is shifted through a custom character set instead of a standard alphabet-only Caesar cipher.

## How to run

From the command line:

```bash
python cipher_encryption_file.py path/to/file.txt
```

The script will then ask you to choose:

1. Encryption mode (`e`) or decryption mode (`d`)
2. A numeric key
3. Whether to save the output with a default file name or a custom name

## Example

```bash
python cipher_encryption_file.py sample.txt
```

Then the script may prompt:

```text
Which mode would you like to do.
To encrypt a file enter 'e' and to decrypt a file enter 'd': e
Enter a key: 3
To save a file in the name you want to give it enter 'new' and to save it using a default name enter 'default' (decryptedData_time.txt): default
```

The output will be written to a new file such as:

- `encryptedData_2026-08-31_12-00-00.txt`

## Notes

- The script only accepts the supported file extensions listed above.
- The key must be a whole number.
- Decryption uses the same key in the opposite direction automatically.
- The output is saved as a new file and does not overwrite the original input file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
