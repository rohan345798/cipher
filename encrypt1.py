def encrypt(m, key):
        a = ''
        for i in m:
                i = i.lower()
                b = key[i]
                a = a + b
        return a

