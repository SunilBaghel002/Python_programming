# Variables
# (EASY)
# Create three variables: name, age, and city. Print them in one line using f-string formatting.
name = "Rohan"
age = 25
city = "Mumbai"
print(f"{name} is {age} years old and living in {city}")

# Assign the same value 100 to three different variables in a single line.
a = b = c = 100
print(f"There are three variables with same value a - {a} \n b - {b} \n c - {c}")

# Define a variable pi = 3.14159. Print the type of the variable, then convert it to an integer and print again.
pi = 3.14159
print(type(pi))
pi = int(pi)
print(f"Value of pi after convert into integer is {pi} and type of pi is {type(pi)}")

# Moderate
# Swap the values of two variables without using a third variable.
num1 = 10
num2 = 20
print(f"Before swapping num1 = {num1} and num2 = {num2}")
num1, num2 = num2, num1
print(f"After swapping num1 = {num1} and num2 = {num2}")

# Take an integer input from the user and store it as a string in another variable. Print both values and their data types.
num3 = int(input("Enter a number : "))
str1 = str(num3)
print(f"Value of integer is {num3} and type of {type(num3)}")
print(f"Value of string is {str1} and type of {type(str1)}")

# Create a variable x = 10. Increase its value by 5, then multiply by 3, then subtract 2 — all in one line (no multiple statements).
x = 10
x = ((x + 5) * 3 ) - 2
print("Result of above expression is:", x)

# Hard Level
# Create three variables a, b, c with numerical values. Write one line of code to rotate their values (i.e., a gets b, b gets c, c gets a).
a = 12
b = 21
c = 34
print(f"a - {a} \n b - {b} \n c - {c}")
a, b, c = b, c, a
print(f"a - {a} \n b - {b} \n c - {c}")

#Take two inputs (string and number) from the user. Multiply the string by the number (example: input "Hi", 3 → output "HiHiHi").
input_str = input("Enter your string : ")
input_num = int(input("enter a number : "))
print(input_str * input_num)

# Write a program to demonstrate mutable vs immutable behavior in Python: Use a list and an integer. Modify both inside a function and show that one changes globally while the other doesn’t.
list1 = [1, 2, 3, 4, 5]
mutable_num = 45

def check():
    list1[0] = 3
    mutable_num = 67
    print(mutable_num)
check()
print(list1)