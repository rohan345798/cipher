def encrypt(m, key):
        a = ''
        for i in m:
                i = i.lower()
                b = key[i]
                a = a + b
        return a


d = {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r', 'j':'q', 'k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'h','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a',' ':' '}
print encrypt('I want mutton',d)
