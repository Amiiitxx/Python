a=input("enter a string:")
digits="0123456789"
d=""
for i in a:
    if i in digits:
        d+=i
print(d)
