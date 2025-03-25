# pylint: disable=C0114
from utils.art import ArtHelper
class CaesarCipher:
    """Caesar cipher class to encrypt and decrypt the text"""
    def __init__(self, mode=0):
        if mode == 0:
            print(ArtHelper.caesar_cipher())

    def encrypt(self, origin_text, shift_amount):
        """Encrypt text using Caesar cipher
        
        Args:
            origin_text (str): The text to be encrypted
            shift_amount (int): The shift amount for the Caesar cipher.
        Returns:
            str: The encoded text after Caesar cipher
        """

        cipher_text = ""
        for char in origin_text:
            letter = char
            if letter.isupper():
                letter = chr((ord(letter) + shift_amount - 65) % 26 + 65)
            elif letter.islower():
                letter  = chr((ord(letter) + shift_amount - 97) % 26 + 97)
            cipher_text += letter

        return cipher_text

    def decrypt(self, cipher_text, shift_amount):
        """Decrypt text using Caesar cipher

        Args:
            cipher_text (str): The text to be decrypted
            shift_amount (int): The shift amount for the Caesar cipher
        Returns:
            str: the decoded text after caesar cipher
        """
        return self.encrypt(cipher_text, -shift_amount)
