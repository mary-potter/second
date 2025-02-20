# Hill Cipher Encryption and Decryption

## Overview
This project implements a **3×3 Hill Cipher** for encryption and decryption. The encryption program reads plaintext from a file (`plain.txt`), generates a key, encrypts the text, and saves both the key and ciphertext. The decryption program reads the key and ciphertext, decrypts the text, and outputs it to a file.

## Files
- `hill_encrypt.py` – Encrypts plaintext using a 3×3 Hill Cipher.
- `hill_decrypt.py` – Decrypts ciphertext using the key.
- `plain.txt` – Input file containing plaintext.
- `cipher.txt` – Output file containing ciphertext.
- `key.txt` – Output file containing the encryption key.
- `decrypted.txt` – Output file containing decrypted text.
- `test_hill_cipher.py` – Unit tests for encryption and decryption.

## Encryption Process
1. Reads plaintext from `plain.txt`.
2. Removes spaces and converts text to lowercase.
3. Generates a random 3×3 key matrix (mod 26).
4. Encrypts text using matrix multiplication.
5. Saves the key in `key.txt` and ciphertext in `cipher.txt`.

## Decryption Process
1. Reads the key from `key.txt` and ciphertext from `cipher.txt`.
2. Computes the modular inverse of the key matrix.
3. Decrypts ciphertext using matrix multiplication.
4. Outputs decrypted text to `decrypted.txt`.

## Running the Programs
### Encrypt Text:
```sh
python hill_encrypt.py
```
### Decrypt Text:
```sh
python hill_decrypt.py
```

## Unit Testing
Run the tests using:
```sh
python -m unittest test_hill_cipher.py
```

## Notes
- The key matrix must be invertible mod 26.
- If the plaintext length is not a multiple of 3, it is padded with 'x'.
- Ensure `numpy` is installed (`pip install numpy`).

