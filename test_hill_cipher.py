import unittest
import numpy as np
from hill_encrypt import encrypt, generate_key
from hill_decrypt import decrypt, mod_inverse

class TestHillCipher(unittest.TestCase):
    
    def setUp(self):
        # Generate a random valid key for testing
        self.key = generate_key()
        self.plaintext = "hello"
        
        # Ensure the plaintext length is a multiple of 3 (Hill cipher block size)
        while len(self.plaintext) % 3 != 0:
            self.plaintext += 'x'  # Padding
        
        self.ciphertext = encrypt(self.plaintext, self.key)
    
    def test_encryption_decryption(self):
        """Test that decryption correctly restores the original plaintext."""
        decrypted_text = decrypt(self.ciphertext, self.key)
        self.assertEqual(decrypted_text, self.plaintext)
    
    def test_key_invertibility(self):
        """Test that the generated key has an inverse in mod 26."""
        key_inv = mod_inverse(self.key, 26)
        self.assertIsNotNone(key_inv)
    
    def test_ciphertext_length(self):
        """Test that the ciphertext length matches the plaintext length."""
        self.assertEqual(len(self.ciphertext), len(self.plaintext))

if __name__ == "__main__":
    unittest.main()
