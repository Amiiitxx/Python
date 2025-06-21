# for i in range(0,21):
#     print (i)

# for i in range (0,21,2):
#     print (i)


n=int(input("Enter a number :"))
oddsum=0
evensum=0
for i in range (n+1):
    if i %2==0:
        evensum+=i
    print (oddsum)
else:
    print(evensum)
