alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



# def encrypt(text, shift):
#     encrypt_text = ""
#     for letter in text:
#         ## Don't use .index
#         # for i in range(0, len(alphabet)):
#         #     if letter == alphabet[i]:
#         #         encrypt_text += alphabet[i+shift]
#         ##
#
#         position = alphabet.index(letter)
#         new_position = position + shift
#         if new_position > 25:
#             new_position -= 26
#         encrypt_text += alphabet[new_position]
#
#     print(encrypt_text)
#
# def decrypt(text, shift):
#     encrypt_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
# #        print(new_position)
#         if new_position < 0:
#             new_position += 26
# #            print(new_position)
#         encrypt_text += alphabet[new_position]
#
#     print(encrypt_text)

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Wrong type!")

def ceasar(text, shift):
    encrypt_text = ""

    if direction == "decode" :
        shift *= -1

    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position > 25:
            new_position -= 26

        encrypt_text += alphabet[new_position]

    print(encrypt_text)

ceasar(text, shift)