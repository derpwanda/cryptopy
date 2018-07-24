def alphabet_position(letter):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    letter = letter.lower()
    return alpha. index(letter)

def rotate_character(char, rot):
    if char.isalpha(): #ignore char that are NOT letters
        rotat_posit = (alphabet_position(char) + rot) % 26 #new rotated position
        position = int(rotat_posit) + ord('a') #new rototated position + ascii 97
        if char.isupper():
            return chr(position).upper()
        else:
            return chr(position) #convert int(position) back to letter
    else:
        return char

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

mess = input('Type a message: ')
key = input('Encryption key: ')
print(encrypt(mess, key))
