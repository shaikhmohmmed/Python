# Euclidean Distance Formula

x1 = int(input("Enter the firt  x-axis = "))
y1 = int(input("Enter the firt  y-axis = "))
x2 = int(input("Enter the second x-axis = "))
y2 = int(input("Enter the second y-axis = "))
distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(f"Distance between points {x1}, {y1} and {x2}, {y2} is {distance}")