n=input("Enter a name: ")
a=input("Enter a charecter:")
count=0
for i in n:
    if i==a:
        count+=1
print("The occurece of the charecter is :",count)