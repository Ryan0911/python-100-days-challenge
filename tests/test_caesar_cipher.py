# pylint: disable=C0114
import unittest
from day_008_caesar_cipher.caesar_cipher import CaesarCipher

class TestCaesarCipher(unittest.TestCase):
    """Unit tests for the day 8 project - Caesar Cipher"""

    def setUp(self):
        """Setup method to initialize the CaesarCipher instance before each test"""
        self.caesar_cipher = CaesarCipher(1)

    def test_encrypt(self):
        """Test the encryption method of the Caesar cipher"""
        self.assertEqual(self.caesar_cipher.encrypt("hello", 5), "mjqqt")
        self.assertEqual(self.caesar_cipher.encrypt("hello", 0), "hello")
        self.assertEqual(self.caesar_cipher.encrypt("hello", 26), "hello")
        self.assertEqual(self.caesar_cipher.encrypt("hello", 27), "ifmmp")
        self.assertEqual(self.caesar_cipher.encrypt("hello", -5), "czggj")
        self.assertEqual(self.caesar_cipher.encrypt("hello", -27), "gdkkn")
        self.assertEqual(self.caesar_cipher.encrypt("hello", -26), "hello")
        self.assertEqual(self.caesar_cipher.encrypt("hello", -0), "hello")

    def test_decrypt(self):
        """Test the decryption method of the Caesar cipher"""
        self.assertEqual(self.caesar_cipher.decrypt("mjqqt", 5), "hello")
        self.assertEqual(self.caesar_cipher.decrypt("hello", 0), "hello")
        self.assertEqual(self.caesar_cipher.decrypt("hello", 26), "hello")
        self.assertEqual(self.caesar_cipher.decrypt("ifmmp", 27), "hello")
        self.assertEqual(self.caesar_cipher.decrypt("czggj", -5), "hello")
        self.assertEqual(self.caesar_cipher.decrypt("gdkkn", -27), "hello")
        self.assertEqual(self.caesar_cipher.decrypt("hello", -26), "hello")
        self.assertEqual(self.caesar_cipher.decrypt("hello", -0), "hello")
    
    def test_encypt_decrypt(self):
        """Test the encryption and decryption methods together"""
        text = "Hello, World!"
        shift = 5
        encrypted_text = self.caesar_cipher.encrypt(text, shift)
        decrypted_text = self.caesar_cipher.decrypt(encrypted_text, shift)
        self.assertEqual(text, decrypted_text)

if __name__ == '__main__':
    unittest.main(verbosity=2)
