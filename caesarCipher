alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#arrayText = list(text)
#print(arrayText)

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    encrypted_message = ""
    for letter in original_text:
        for congruency in alphabet:
            if letter == congruency:
                cipher = alphabet.index(letter) + shift_amount
                while cipher > 26:
                        shift_amount -= 1
                        cipher = alphabet.index('a') + shift_amount - 1
                        #print(cipher)
                encrypted_message += alphabet[cipher]
    print(f"Here is the encrypted code: {encrypted_message}", end="")


encrypt(text, shift)
