# pylint: disable=C0114, C0103, C0301
from caesar_cipher import CaesarCipher

caesar_cipher = CaesarCipher()

continue_or_not = 'yes'
while continue_or_not.lower() == 'yes':
    direction = ""
    text = ""
    shift = -1

    while direction not in ['encode', 'decode']:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while not text:
        text = input("Type your message:\n").strip()
    while not (isinstance(shift, int) and shift > 0):
        try:
            shift = int(input("Type the shift number (positive integer):\n"))
            if shift <= 0:
                print("Shift number must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")

    if direction == 'encode':
        print(f"Here is the encoded result: {caesar_cipher.encrypt(text, shift)}")
    else:
        print(f"Here is the decoded result: {caesar_cipher.decrypt(text, shift)}")

    continue_or_not = input("If you want to continue, type 'yes'. Otherwise, press any key to exit.\n")
print("Goodbye!")
