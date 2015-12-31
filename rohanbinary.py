m = int(raw_input('put in a num'))
l = []
a = m
i = 1
while a != 1:
    if a <= 0:
        print 0
        break
    i = a%2
    l.insert(0,i)
    if a/2 == 1:
        l.insert(0,1)
    a = a/2

for i in l:
    print i,
