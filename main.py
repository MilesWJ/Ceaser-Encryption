import string

text = str(input("Enter the text you would like to encrypt: ")).lower()
shift = int(input("Enter the shift you would like: "))

alphabet = string.ascii_lowercase
shifted_alphabet = alphabet[shift:] + alphabet[:shift]

table = str.maketrans(alphabet, shifted_alphabet)


def encrypt():
    encrpyted_text = text.translate(table)
    print(encrpyted_text)


while True:
    encrypt()
