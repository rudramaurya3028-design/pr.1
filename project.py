print("WELCOME TO THE BILL SPLITTER APP !")
print()
bill_amount = float(input("Enter the total bill amount :"))
people = int(input("Enter the number of people  :"))
if people <= 0:
    print("Number of people must be greater than zero.")
    exit()
tip_percent = float(input("Enter the tip percentage :"))
if tip_percent < 0:
    print("Tip percentage is invalid.")
    exit()
print()
Tip_amount = bill_amount * tip_percent / 100
Final_Bill = bill_amount + Tip_amount
Per_Person = Final_Bill / people
print()
print("Total bill amount : $", bill_amount)
print("Tip amount : $", Tip_amount)
print("Final bill amount : $", Final_Bill)
print("Amount per person : $", Per_Person)
print("THANK YOU FOR USING THE BILL SPLITTER APP !")
print(    )
while True:
    print("Would you like to calculate  another bill ? (y/n)")
    
    if input().lower() == 'y':