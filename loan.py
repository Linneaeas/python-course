
money_owed=float(input("How much money do you owe, in dolllars?\n"))
apr = float(input("what is the annual percentage rate of the loan?\n"))
payment = float(input("How much money will you pay off each month in dollars?\n"))
months = int(input("How many month do you want to see results for?\n"))

monthly_rate = apr/100/12

for i in range(months):
  #Calculate interest to pay
  interest_paid=money_owed*monthly_rate
  #Add in interest
  money_owed=money_owed+interest_paid

  if (money_owed - payment < 0 ):
      print("The last payment is", money_owed)
      print("You paid off the loan in", i+1, "months")
      break

#Make payment
money_owed=money_owed-payment

print("Paid", payment,"of which", interest_paid, "was interest", end=" ")
print("Now I owe", money_owed)