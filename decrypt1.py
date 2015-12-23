# decrypt will decrypt a message(m) with a key(key)
def decrypt(msg, k):
# decrypt will take the message and change it to the regular alphabet with the key
# it will keep doing this until the message is decrypted
    y=''
    for i in msg:
        print 'i :',i         
        v = k[i]
        print 'v :',v
        y= y + v
        print 'y :',y

    return y


key = {'z':'a','p': 'b','i':'s','a':'x','':''}
print decrypt('pizza',key)
