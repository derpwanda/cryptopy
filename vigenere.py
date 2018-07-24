from helpers import alphabet_position, rotate_character

def encrypt(text, cipher):
    encrypt_text = ''
    rotated_index = 0
    for i in text:
        if i.isalpha():
            w = alphabet_position(cipher[rotated_index % len(cipher)])
            encrypt_text = encrypt_text + rotate_character(i, w) #can't convert int to str
            rotated_index = rotated_index + 1
        else:
            encrypt_text = encrypt_text + rotate_character(i, w)

    return encrypt_text

#mess = input('Type a message: ')
#key = input('Encryption key: ')
#print(encrypt(mess, key))
