print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")
print("Choose your operator")

operator=input()

if operator=="1" :
    num1=float(input("Put the first number"))
    num2=float(input("Put the second number"))
    print(num1+num2)
elif operator=="2" :
    num11=float(input("Put the first number"))
    num22=float(input("Put the second number"))
    print(num11-num22)
elif operator=="3" :
    num3=float(input("Put the first number"))
    num4=float(input("Put the second number"))
    if num4==0 :
        print("Math error")
    else :
     print(num3/num4)
elif operator=="4" :
    num33=float(input("Put the first number"))
    num44=float(input("Put the second number"))
    print(num33*num44)
else :
    print("Try agian")

