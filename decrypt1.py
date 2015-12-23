# decrypt will decrypt a message(m) with a key(key)
def decrypt(msg, k):
# decrypt will take the message and change it to the regular alphabet with the key
# it will keep doing this until the message is decrypted
      y = ''
      for l in msg:
        # covert to lowercase becuase it was giving error
        l = l.lower()
        print 'l :',l
        v = k[l]
        print 'v :',v
        y = y + v
        print 'y :',y

      return y

    
key = {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r', 'j':'q', 'k':'p','l':'o',
       'm':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'h','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a',' ':' '}
someinput = raw_input('please enter a message :')
print decrypt(someinput,key) 
