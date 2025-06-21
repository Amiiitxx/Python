l=[1,2,2,3,4,4,5]
b=[]
c=[]
for i in l:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
print(b,c)