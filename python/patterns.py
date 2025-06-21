# a=int(input("Enter a num: "))
# for i in range(a):
#     print("*"*i)



# a=int(input("enter a num: "))
# for i in range(a,0,-1):
#     print("&"*i)

# a=int(input("enter a num:"))
# for i in range(a+1):
#     print(" "*(a-i),"*"*i)


# a=int(input("enter a num:"))
# for i in range(a,0,-1):
#     print(" "*(a-i),"*"*i)


# a=int(input("Enter a num :"))
# for i in range(a,0,-1):
#     print(" "*(a-i),"*"*(2*i-1))


# a=int(input("enter a num :"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# a=int(input("enter a num :"))
# for i in range(a,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()



# a=int(input("entr a num :"))
# for i in range(1,a+1):
#     print(" "*(a-i),end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()




# a=int(input("entr a num :"))
# for i in range(1,a+1):
#     print(" "*(a-i),end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# for i in range(a-1,0,-1):
#     print(" "*(a-i),end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()





a=int(input("enter a range:"))
for i in range(1,a+1):
    print(" "*(a-i),end="")
    ch=65
    for j in range(i):
        print(chr(ch),end=" ")
        ch+=1
    print()
for i in range(a-1,0,-1):
    print(" "*(a-i),end="")
    ch=65
    for j in range(i):
        print(chr(ch),end=" ")
        ch+=1
    print()