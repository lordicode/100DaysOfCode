alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text_message, shift_by, direction):
    string_for_cipher = ""
    if direction == "encode":
        for letter in text_message:
            position = alphabet.index(letter)
            new_position = position + shift_by
            encrypted_letter = alphabet[new_position]
            string_for_cipher += encrypted_letter
    elif direction == "decode":
        for letter in text_message:
            position = alphabet.index(letter)
            new_position = position - shift_by
            encrypted_letter = alphabet[new_position]
            string_for_cipher += encrypted_letter
    print(f"Resulting text is {string_for_cipher}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(text_message=text, shift_by=shift, direction=direction)
