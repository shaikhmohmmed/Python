num = int(input("Enter the number: "))

if  num < 0:
    print("Enter the positive number.")
else:
    sum = 0
    while  (num > 0):
        sum +=num
        num -= 1
    print(f"The sum is: {sum}")
    