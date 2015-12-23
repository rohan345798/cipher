# decrypt will decrypt a message(m) with a key(key)
def decrypt(encrypt, key):
# decrypt will take the message and change it to the regular alphabet with the key
# it will keep doing this until the message is decrypted
    l= len(encrypt)
    while (l != 0):
        if encrypt[l] == 'a':
            encrypt[1] = 'z'
            l = l - 1#this is a one on the left
            return encrypt
