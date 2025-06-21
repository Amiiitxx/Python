a=float(input("Enter BMI : "))
if a<18.5:
    print("Under weight")
elif a>18.5 and a<25:
    print("Normal") 
elif a>=25 and a<30:
    print("over wheight")
elif a>=30:
    print ("obesity")