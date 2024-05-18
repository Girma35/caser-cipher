alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
def encrypt(plain_text, shift_amount):
    display = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            display += new_letter
        else:
            display += letter
    print(f"The encoded text is: {display}")

def decrypt(cipher_text, shift_amount):
    display = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            new_letter = alphabet[new_position]
            display += new_letter
        else:
            display += letter
    print(f"The decoded text is: {display}")
def all():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Invalid input! Please type 'encode' or 'decode'.")
all()
end_program =input(f"Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if end_program == 'yes':
    all()
else :
    print("Goodbye!")
    