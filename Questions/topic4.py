# Conditional Statements
# Easy level
# Take a number from the user and print whether it is positive, negative, or zero.
num = int(input("Enter a number : "))
if num > 0 :
    print(f"{num} is a positive number")
elif num < 0 :
    print(f"{num} is a negative number")
else :
    print(f"{num} is zero")

# Write a Python program to check whether a person is eligible to vote or not (age ≥ 18).
user_age = int(input("Enter your age : "))
if user_age >= 18 and user_age <= 120:
    print("You are eligible to vote")
elif user_age >= 0 and user_age < 18 :
    print("You are not eligible to vote")
else:
    print("Please input a correct age.")

# Take a number from the user and print whether it is even or odd using an if–else statement.
num1 = int(input("Enter a number : "))
if num1 % 2 == 0:
    print(f"{num1} is a even number")
else:
    print(f"{num1} is a odd number")

# Moderate Level
# Write a Python program to find the largest of three numbers using nested if–else.
a = 10
b = 20
c = 15
if a > b and a > c:
    print(f"a - {a} is a largest number")
elif b > a and b > c:
    print(f"b - {b} is a largest number")
else:
    print(f"c - {c} is a largest number")

# Take a year as input and check whether it is a leap year or not.
input_year = int(input("Enter a year : "))
if input_year > 0:
    if input_year % 4 == 0:
        print(f"{input_year} is a leap year")
    else:
        print(f"{input_year} is not a leap year")
else:
    print("Please input a correct year.")

# Take marks as input and print the grade based on this logic:
marks1 = int(input("Enter marks of first subject : "))
marks2 = int(input("Enter marks of second subject : "))
marks3 = int(input("Enter marks of third subject : "))

avg = (marks1 + marks2 + marks3) / 3

if avg < 100:
    if avg <= 100 and avg >= 90:
        print("Your grade is A")
    elif avg < 90 and avg >= 80:
        print("Your grade is B")
    elif avg < 80 and avg >= 70:
        print("Your grade is C")
    elif avg < 70 and avg >= 60:
        print("Your grade is B")
    else:
        print("Your grade is F")
else:
    print("Please input marks out of 100")

# Hard Level
# Take input of three sides of a triangle and determine: If it is equilateral, isosceles, or scalene.
side_1 = int(input("Enter first side of triangle : "))
side_2 = int(input("Enter second side of triangle : "))
side_3 = int(input("Enter third side of triangle : "))

if side_1 == side_2 == side_3 :
    print(f"Triangle formed by {side_1}, {side_2}, {side_3} is equilateral triangle") 
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print(f"Triangle formed by {side_1}, {side_2}, {side_3} is isosceles triangle")
else:
    print(f"Triangle formed by {side_1}, {side_2}, {side_3} is scalene triangle")

# Create a simple calculator program using if–elif–else that performs +, -, *, / based on the user’s choice.
num2 = int(input("Enter a number for calculator : "))
num3 = int(input("Enter second number for calculator : "))
user_choice = input("Enter operation which you want to perform +, - /, * : ")

if user_choice == '+':
    print(f"Sum of {num2} and {num3} is {num2 + num3}")
elif user_choice == '-':
    print(f"Difference of {num2} and {num3} is {num2 - num3}")
elif user_choice == '*':
    print(f"product of {num2} and {num3} is {num2 * num3}")
elif user_choice == '/':
    print(f"Division of {num2} and {num3} is {round(num2 / num3, 2)}")
else:
    print("Please enter a valid operation")

# Take an integer input and check: If divisible by 2 and 3 → print "Divisible by both", If divisible by only 2 → print "Divisible by 2", If divisible by only 3 → print "Divisible by 3", Otherwise → print "Not divisible by 2 or 3"
integer_input = int(input("Enter an integer : "))

if integer_input % 2 == 0 and integer_input % 3 == 0:
    print(f"{integer_input} is Divisible by both")
elif integer_input % 2 == 0:
    print(f"{integer_input} is Divisible by 2")
elif integer_input % 3 == 0:
    print(f"{integer_input} is Divisible by 3")
else:
    print(f"{integer_input} is Not divisible by 2 or 3")