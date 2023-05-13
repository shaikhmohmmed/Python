# 1. If unit consumed <= 100 then cost per unit is Rs 3.46
# 2. If unit consumed >= 101 and <= 300 then cost per unit is Rs 7.43
# 3. If unit consumed >= 301 and <= 500 then cost per unit is Rs 10.32
# 4. If unit consumed >= 501 then the cost per unit is Rs 11.71
# 5. Line rent is Rs 1.45 per unit.
# 6. Additional fixed Meter rent is Rs 100.
# 7. The tax on the bill is 16 percent which can be taken as 0.16.

unit = int(input('Enter the unit: '))
if unit <=100 :
    bill = unit * 3.64
elif unit >=101 and  unit <= 300:
    bill = 364 + ((unit - 100)*7.43)
elif unit >= 301 and  unit <= 500:
    bill = 364 + 1486 + ((unit - 300 )* 10.32)
else:
    bill = 364 + 1486 + 2064+  ((unit - 500)*11.71) 
print(f"Bill per unit: {bill}")
bill = bill * (unit*1.45)
print(f"Bill after adding Line rent: {bill}")
bill = bill + 100
print(f"Bill after adding meter rent: {bill}")
bill = bill + (bill*0.16)
print(f"Total bill after adding taxt = {bill}")