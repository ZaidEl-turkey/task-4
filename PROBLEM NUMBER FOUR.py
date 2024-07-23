
total_prchaes= float(input("Enter the total purchaes amount :"))
years_membership= float(input("Enter the number of years of membership :"))
coplaints_pastyear= float(input("Enter the number of coplaints filed in the past year :"))
purchase_pastyear= float(input("Enter the number of purchases made in the past year :"))

discount=0
dis=coplaints_pastyear*2

if years_membership>10 : 
      discount=discount+10
elif 6<=years_membership<=10 :
       discount=discount+8-dis
elif years_membership<6 :
     discount=discount+5

discount=discount-dis  

if discount<0 :
    discount=0

if purchase_pastyear>20 :
    discount=discount + 5

net_discount=total_prchaes-(total_prchaes-discount/100*total_prchaes)
total=total_prchaes-discount/100*total_prchaes
  
print("Net discount amount: "+str(net_discount))
print("New total purchase: " + str(total))
