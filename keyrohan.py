def keygen():
    #ask user for a number
    #make dict and every letter is pushed number places to the left, so z would be g, y would be f, a would be h, and so on
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','l','o','p','q','r','s','t','u','v','w','x','y','z']
    keylist = []
    n = int(raw_input('put in a number,1 to 25: '))
    while n < 1 or n > 25:
        try:
            n = int(raw_input('put in a number,1 to 25:: '))
        except:
            print 'put in a number'
    for i in l:
        keylist.append(l[i + n%26])
    print keylist
    
print keygen()
        
    
