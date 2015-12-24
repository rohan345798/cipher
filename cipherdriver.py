from key import key
from encrypt1 import encrypt
from decrypt1 import decrypt
d = key()
msg = str(raw_input('enter a message: '))
print encrypt(msg,d)
print decrypt(encrypt(msg,d), d)
