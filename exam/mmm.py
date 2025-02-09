a = list()
a = [None, 1, 2, 3, None, 4, None, None]
x = None
for i in range(len(a)):
    if a[i] in a:
        if a[i] != None:
            x = a[i]
        elif a[i] == None:
            a[i] = x
            
print(a)