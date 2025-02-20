import numpy as np
import string
import random

# Function to compute modular inverse of a matrix in mod 26
def mod_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix)))  # Compute determinant
    det_inv = pow(det, -1, mod)  # Compute modular inverse of determinant
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod  # Compute adjugate matrix
    return (det_inv * adjugate) % mod  # Return modular inverse matrix

# Function to generate a valid 3x3 key matrix
def generate_key():
    while True:
        key = np.random.randint(0, 26, (3, 3))  # Generate random 3x3 matrix
        if np.gcd(int(round(np.linalg.det(key))), 26) == 1:  # Ensure determinant is invertible mod 26
            return key

# Function to convert text into numerical representation
def text_to_numbers(text):
    return [string.ascii_lowercase.index(c) for c in text if c in string.ascii_lowercase]

# Function to convert numbers back to text
def numbers_to_text(numbers):
    return ''.join(string.ascii_lowercase[n] for n in numbers)

# Function to encrypt plaintext using Hill Cipher
def encrypt(text, key):
    text = text.lower().replace(" ", "").replace("\n", "")  # Preprocess text (remove spaces and newlines)
    while len(text) % 3 != 0:
        text += 'x'  # Padding to make length a multiple of 3
    
    text_numbers = text_to_numbers(text)  # Convert text to numbers
    text_matrix = np.array(text_numbers).reshape(-1, 3).T  # Convert into 3xN matrix
    
    cipher_matrix = (key @ text_matrix) % 26  # Matrix multiplication and mod 26 operation
    cipher_numbers = cipher_matrix.T.flatten()  # Convert back to 1D list
    return numbers_to_text(cipher_numbers)  # Convert numbers back to text

if __name__ == "__main__":
    # Read plaintext from file
    with open("plain.txt", "r") as f:
        plaintext = f.read().strip()
    
    key = generate_key()  # Generate encryption key
    ciphertext = encrypt(plaintext, key)  # Encrypt the plaintext
    
    # Save the key to file
    with open("key.txt", "w") as f:
        for row in key:
            f.write(" ".join(map(str, row)) + "\n")
    
    # Save the ciphertext to file
    with open("cipher.txt", "w") as f:
        f.write(ciphertext)
    
    print("Encryption completed. Key saved in 'key.txt', Ciphertext saved in 'cipher.txt'.")
