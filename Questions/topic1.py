# Write a Python program to print: Hello, Sunil! Welcome to Python.
print("Hello, Sunil! Welcome to Python.")

# Take two inputs from the user (your name and age) and display them in a formatted sentence.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
print(f"My name is {name} and I am {age} year old.")

# Display the data type of the following variables
a = 5
b = 3.14
c = "Python"
d = True
e = [1, 2, 3]
print(type(a), type(b), type(c), type(d), type(e))

#Take a user’s full name as input and print it in: Uppercase, Lowercase, Title case

full_name = input("Enter your full name : ")
print(f"UpperCase of {full_name} is", full_name.upper())
print(f"LowerCase of {full_name} is", full_name.lower())
print(f"Title Case of {full_name} is", full_name.title())

# Write a Python program to convert temperature from Celsius to Fahrenheit.
input_celsius = float(input("Enter a celsius value which you want to convert to fahrenheit : "))
result = (9*input_celsius)/5 + 32
print(f"Coversion of {input_celsius}°C is {result}°F")

# Ask the user to enter two numbers and display their sum, difference, mutiply, Division
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(f"Sum of {num1} and {num2} is {num1 + num2}")
print(f"Difference of {num1} and {num2} is {num1 - num2}")
print(f"Product of {num1} and {num2} is {num1 * num2}")
result_1 = float(num1 / num2)
print(f"Division of {num1} and {num2} is {result_1}")


# Take the user’s name and age as input and print how many years are left until they turn 100 years old.
# Name and age are already take as input above
remaining_age = 100 - age
print(f"{name} will turn 100 years old in {remaining_age} years.")

# Ask the user to enter a number and display whether it is positive, negative, or zero — without using if-else directly (try using dictionary mapping or ternary operators).
num3 = int(input("Enter a number : "))
if num3>0:
    print(f"{num3} is a positive number")
elif num3<0:
    print(f"{num3} is a negative number")
else:
    print(f"{num3} is zero")
    
# Write a single-line Python statement that prints: Hello from Python, version 3.x! — where the version number is fetched automatically from the sys module.
import sys
print("Hello from Python, version", sys.version)