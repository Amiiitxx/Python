n=int(input("Enter a number: "))
a=True
if n<2:
    a=False
for i in range(2,n):
    if n % 2 ==0:
        a=False
        break
if a== True:
    print("prime")
else:
    print("not")


