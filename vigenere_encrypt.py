import string

def vigenere_encrypt(plaintext, key):
    """Encrypts the given plaintext using the Vigenère cipher with the provided key."""
    alphabet = string.ascii_lowercase
    plaintext = plaintext.lower().replace(" ", "").replace("\n", "")  # Normalize text
    key = key.lower()
    
    encrypted_text = ""
    key_index = 0
    
    for char in plaintext:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            new_index = (alphabet.index(char) + shift) % 26
            encrypted_text += alphabet[new_index]
            key_index += 1
        else:
            encrypted_text += char  # Keep non-alphabet characters unchanged
    
    return encrypted_text

if __name__ == "__main__":
    # Read plaintext from file
    with open("plain.txt", "r") as f:
        plaintext = f.read().strip()
    
    # Define encryption key (Modify as needed)
    key = "securekey"
    
    # Encrypt text
    ciphertext = vigenere_encrypt(plaintext, key)
    
    # Save the key to file
    with open("key.txt", "w") as f:
        f.write(key)
    
    # Save the ciphertext to file
    with open("cipher.txt", "w") as f:
        f.write(ciphertext)
    
    print("Encryption completed. Key saved in 'key.txt', Ciphertext saved in 'cipher.txt'.")
