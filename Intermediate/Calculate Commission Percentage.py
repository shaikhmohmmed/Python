
# Comission Percentage 

keep_going='y'

while keep_going=='y':
    sales=float(input('Enter the amount of sales: '))
    comm_rate=float(input('Enter commission rate: '))
    total=0
    commission=sales*comm_rate
    print(f"commission is {commission}")
    keep_going=input("Enter 'y' for keep going and 'n' for stop: ")
    total=total+commission
    print(f"Total is {total}")
print(f"You have exited the program. The total is {total}")