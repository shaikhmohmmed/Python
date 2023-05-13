#  Amount          Discount
#     0-5000          5%
#     5000-15000      12%
#     15000-25000     20%
#     above 25000     30%

amount = int(input("Enter the amount: "))

if amount<=0 :
    print("There is no amount you have paid.")
elif amount<= 5000:
    dis = amount * 0.05
elif amount <= 15000:
    dis = amount * 0.12
elif amount <= 25000:
    dis = amount* 0.2
else:
    dis = amount * 0.3
    

print(f"Discount= {int(dis)}")
print(f"Net Price= {amount - dis}")