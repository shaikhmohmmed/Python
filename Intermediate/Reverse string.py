def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = input("Enter the string: ")
print(f"The original string is : {s}")
print(f"The reversed string is : {reverse(s)}")