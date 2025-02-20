# Vigenère Cipher Encryption and Decryption

## Overview
This project implements the **Vigenère Cipher** for encryption and decryption using text files. The encryption program reads plaintext from a file (`plain.txt`), encrypts it using a given key, and writes the ciphertext to `cipher.txt`. The decryption program reads the ciphertext and key from files and outputs the decrypted plaintext.

## Files
- `vigenere_encrypt.py` – Encrypts plaintext using the Vigenère Cipher.
- `vigenere_decrypt.py` – Decrypts ciphertext using the key.
- `plain.txt` – Input file containing plaintext.
- `cipher.txt` – Output file containing ciphertext.
- `key.txt` – Output file containing the encryption key.
- `decrypted.txt` – Output file containing decrypted text.
- `test_vigenere_cipher.py` – Unit tests for encryption and decryption.

## Encryption Process
1. Reads plaintext from `plain.txt`.
2. Removes spaces and converts text to lowercase.
3. Encrypts text using a predefined key with the Vigenère cipher.
4. Saves the key in `key.txt` and ciphertext in `cipher.txt`.

## Decryption Process
1. Reads the key from `key.txt` and ciphertext from `cipher.txt`.
2. Uses the Vigenère cipher to decrypt the text.
3. Outputs the decrypted text to `decrypted.txt`.

## Running the Programs
### Encrypt Text:
```sh
python vigenere_encrypt.py
```
### Decrypt Text:
```sh
python vigenere_decrypt.py
```

## Unit Testing
Run the tests using:
```sh
python -m unittest test_vigenere_cipher.py
```

## Notes
- The key should be chosen carefully to ensure proper encryption and decryption.
- Only alphabetical characters are encrypted; spaces and special characters are ignored.
- Ensure `plain.txt` contains only text data for proper encryption.

