import numpy as np
import string

def mod_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, mod)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    return (det_inv * adjugate) % mod

def text_to_numbers(text):
    return [string.ascii_lowercase.index(c) for c in text if c in string.ascii_lowercase]

def numbers_to_text(numbers):
    return ''.join(string.ascii_lowercase[n] for n in numbers)

def decrypt(ciphertext, key):
    key_inv = mod_inverse(key, 26)  # Compute modular inverse of the key
    cipher_numbers = text_to_numbers(ciphertext)  # Convert ciphertext to numbers
    cipher_matrix = np.array(cipher_numbers).reshape(-1, 3).T  # Convert into 3xN matrix
    
    plain_matrix = (key_inv @ cipher_matrix) % 26  # Matrix multiplication and mod 26 operation
    plain_numbers = plain_matrix.T.flatten()  # Convert back to 1D list
    return numbers_to_text(plain_numbers)  # Convert numbers back to text

if __name__ == "__main__":
    # Read the key from file
    with open("key.txt", "r") as f:
        key = np.array([list(map(int, line.split())) for line in f])
    
    # Read the ciphertext from file
    with open("cipher.txt", "r") as f:
        ciphertext = f.read().strip()
    
    plaintext = decrypt(ciphertext, key)  # Decrypt the text
    
    # Save the decrypted text to file
    with open("decrypted.txt", "w") as f:
        f.write(plaintext)
    
    print("Decryption completed. Decrypted text saved in 'decrypted.txt'.")
