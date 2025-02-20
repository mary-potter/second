import string

def vigenere_decrypt(ciphertext, key):
    """Decrypts the given ciphertext using the Vigenère cipher with the provided key."""
    alphabet = string.ascii_lowercase
    ciphertext = ciphertext.lower()
    key = key.lower()
    
    decrypted_text = ""
    key_index = 0
    
    for char in ciphertext:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            new_index = (alphabet.index(char) - shift) % 26
            decrypted_text += alphabet[new_index]
            key_index += 1
        else:
            decrypted_text += char  # Keep non-alphabet characters unchanged
    
    return decrypted_text

if __name__ == "__main__":
    # Read the key from file
    with open("key.txt", "r") as f:
        key = f.read().strip()
    
    # Read the ciphertext from file
    with open("cipher.txt", "r") as f:
        ciphertext = f.read().strip()
    
    # Decrypt text
    decrypted_text = vigenere_decrypt(ciphertext, key)
    
    # Save the decrypted text to file
    with open("decrypted.txt", "w") as f:
        f.write(decrypted_text)
    
    print("Decryption completed. Decrypted text saved in 'decrypted.txt'.")
