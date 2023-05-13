# Calculate Average Of N Numbers
n = int(input("Enter value: "))
sum = 0

for num in range(1, n + 1):
    sum = sum + num  
average = sum / n
print(f"Average of {n} numbers is: {average}")
