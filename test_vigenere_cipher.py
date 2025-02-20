import unittest
from vigenere_encrypt import vigenere_encrypt
from vigenere_decrypt import vigenere_decrypt

class TestVigenereCipher(unittest.TestCase):
    
    def setUp(self):
        self.key = "securekey"
        self.plaintext = "hello world"
        self.encrypted_text = vigenere_encrypt(self.plaintext, self.key)
    
    def test_encryption_decryption(self):
        """Test that decryption correctly restores the original plaintext."""
        decrypted_text = vigenere_decrypt(self.encrypted_text, self.key)
        self.assertEqual(decrypted_text, self.plaintext.replace(" ", ""))
    
    def test_ciphertext_length(self):
        """Test that the ciphertext length matches the plaintext length (ignoring spaces)."""
        self.assertEqual(len(self.encrypted_text), len(self.plaintext.replace(" ", "")))

if __name__ == "__main__":
    unittest.main()
