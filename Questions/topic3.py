# Operators
# Easy
# Take two numbers as input and print their: Sum, Difference, Product, Quotient, Modulus
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print(f"Sum of {num1} and {num2} is {num1 + num2}")
print(f"Difference of {num1} and {num2} is {num1 - num2}")
print(f"Product of {num1} and {num2} is {num1 * num2}")
print(f"Division of {num1} and {num2} is {num1 / num2}")
print(f"Modulus of {num1} on {num2} is {num1 % num2}")

# Write a Python program to compare two numbers and print: True if they are equal, False otherwise
if num1 == num2:
    print(f"{num1} and {num2} are equal, True")
else:
    print("False")

# Take a number and check if it is even or odd using the modulus operator (%).
num3 = int(input("Enter a number : "))
if num3 % 2 == 0:
    print(f"{num3} is even number")
else:
    print(f"{num3} is odd number")


# Moderate Level
# Write a Python program that checks if a number is divisible by both 3 and 5 using logical operators.
num4 = int(input("Enter a number to check whether it is divisible by 3 and 5 : "))
if(num4 % 3 == 0 and num4 % 5 == 0):
    print(f"{num4} is divisible by both 3 and 5")
else:
    print(f"{num4} is not divisible by both 3 and 5")

# Initialize a = 10. Use compound assignment operators to: Add 5, Multiply by 2, Subtract 4, Divide by 3, Print the value after each operation.
a = 10
print(f"a at first step is {a}")
a = a * 2
print(f"a after first step is {a} - multiplication of 2")
a = a - 4
print(f"a after second step is {a} - subtractation of 4")
a = a / 3
print(f"a after third step is {a} - final result")

# Compare two user inputs (num1 and num2): Print "num1 is greater", "num2 is greater", or "both are equal" using comparison operators.
# i already declare and take input of num1 and num2 above
if num1 > num2:
    print("num1 is greater")
elif num1 < num2:
    print("num2 is greater")
else:
    print("both are equal")

# Hard Level
# Write a Python program to swap two numbers using only arithmetic operators (no third variable, no tuple unpacking).
x = 12
y = 21

print(f"Before swapping : \n x - {x}\n y - {y}")

x = x^y
y = y^x
x = x^y

print(f"After swapping : \n x - {x}\n y - {y}")