a=input("enter a string:")
digits="0123456789"
al=0
digit=0
for i in a:
    if i in digits:
        digit+=1
    else:
        al+=1
print(digit,al)
