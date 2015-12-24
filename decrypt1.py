# decrypt will decrypt a message(m) with a key(key)
def decrypt(msg, k):
# decrypt will take the message and change it to the regular alphabet with the key
# it will keep doing this until the message is decrypted
    y=''
    for i in msg:    
        v = k[i]
        y= y + v

    return y
