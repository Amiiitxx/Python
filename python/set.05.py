a={1,2,3,4}
b={3,4,5,6}
l=[]
for i in a:
    if i not in b:
        l.append(i)
for i in b:
    if i not in a:
        l.append(i)
print(l)