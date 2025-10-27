# # Loops
# # easy level
# # Sum of N Natural Numbers: Write a Python program to calculate the sum of first N natural numbers using a loop.
# num = int(input("Enter a natural number : "))
# result = 0

# if num > 0 :
#     for i in range(1, num+1):
#         result += i
# else:
#     print("Enter a valid natural number")
# print(f"Sum of first {num} natural number is {result}")

# # Factorial Calculator: Ask the user for a number and calculate its factorial using a for loop.
# num1 = int(input("Enter a number to find factorial : "))
# result_1 = 1
# if num1 > 0:
#     for i in range(1, num1 + 1):
#         result_1 *= i
# else:
#     print("please enter a valid number.")
# print(f"Factorial of {num1} is {result_1}")

# # Multiplication Table Generator: Take a number from the user and print its multiplication table up to 10.
# num2 = int(input("Enter a number to print a table : "))
# print(f"Multiplication table for {num2} is:")
# for i in range(1, 11):
#     print(f"{num2} * {i} = {num2 * i}")

# # Reverse a String: Input a string and reverse it using a loop (don’t use Python’s slicing).
# input_str = input("Enter a string : ")
# result_str = ""

# if len(input_str) > 0:
#     for i in input_str:
#         result_str = i + result_str
# else:
#     print("Please enter a string")
# print(f"Reverse of {input_str} is {result_str}")

# # Count Even and Odd Numbers in a List: Given a list of integers, count how many are even and how many are odd using a loop.
# list_1 = [1, 2, 3, 4, 5, 6, 7]
# count_even = 0
# count_odd = 0

# for i in list_1:
#     if i % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
# print(f"Number of even numbers in list {list_1} is {count_even}")
# print(f"Number of odd numbers in list {list_1} is {count_odd}")

# Intermediate Level
# Sum of Digits of a Number: Input an integer and find the sum of its digits using a while loop.
num3 = int(input("Enter a number : "))
result_2 = 0
while num3 > 0:
    digit = num3 % 10
    result_2 += digit
    num3 //= 10
print(f"Sum of digits of {num3} is {result_2}")

# Check for Prime Number: Ask the user for a number and check if it’s a prime using a for loop.
