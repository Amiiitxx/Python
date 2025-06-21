a=input("Enter a letter :")
vowels="aeiou"
b=""
for i in a:
    if i not in vowels:
        b+=i
print(b)
