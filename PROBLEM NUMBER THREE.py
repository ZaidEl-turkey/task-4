loan_amount=float(input("Enter the loan amount"))
age=int(input("Enter your age"))
monthly_income=float(input("Enter your monthly income"))
employed_status=input("Enter your employed status (Employed OR Unemployed)")
credit_score=float(input("Enteryour credit score"))
outstanding=input("Enter your outstanding (YES OR NO)")


if age>=18 and loan_amount>=12 and employed_status=="employed" and 350<=credit_score<=800 and outstanding=="no" :
    print("Congratulations ! You are eligiblr for a loan")
else :
    print("Sorry,you are not eligible for a loan")
    if age<18 :
        print("REASONA : Not old enough")
    if loan_amount<12 :
        print("REASONA : Loan amount below the threshold")
    if employed_status=="unemployed" :
        print("REASONA : Unemployed customers are not eligible")
    if credit_score>800 or credit_score<350 :
        print("REASONA : The accepted range is between 350 and 800")
    if outstanding=="yes" :
        print("REASONA : Should have not outstanding")


