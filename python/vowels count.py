n=(input("Enter a letter:"))
vowels="aeiou"
ccount=0
vcount=0
for i in n:
    if i in vowels:
        vcount+=1
    else:
        ccount+=1
print("vowel count =",vcount)
print("consons count=",ccount)