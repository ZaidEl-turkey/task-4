degree=float(input("ENTER YOUR EXAM DEGREE"))

if 0<=degree<=100 :
    if 90<=degree<=100 :
        print("A")
    elif 80<=degree<=89 :
        print("B")
    elif 70<=degree<=79 :
        print("C")
    elif 60<=degree<=69 :
        print("D")
    elif 0<=degree<=59 :
        print("F")
                        
else :
    print("INVALID DEGREE")