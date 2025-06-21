a=int(input("enter a range:"))
b=set()
for i in range(a):
    x=input("enter a value:")
    b.add(x)
print(b)
l=list(b)
max=min=l[0]
for i in l:
    if max<i:
        max=i
    if min>i:
        min=i
print("the maximum value is :",max,"\nthe minimum value is :",min)
