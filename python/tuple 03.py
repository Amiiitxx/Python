a=(2,3,4,5,6,7,8,4,6,2,6,7,4,8,9,)
# print(a.count(6))

count=0
l=len(a)
x=int(input("enter a num :"))
for i in range(l):
    if a[i]==x:
        count+=1
print(count)