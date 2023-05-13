a = int(input("Enter the value: "))

num1 = 0
num2 = 1
count = 0

if a == 1:
    print("Choosen number is Fibonacci Series. ")
elif a < 0:
    print("Enter the Positive Number.")
else:
    print("Fibonacci Series: ")
    while count < a: 
        num = num1 + num2
        print(num1)
        num1 = num2 
        num2 = num
        count += 1  
     
