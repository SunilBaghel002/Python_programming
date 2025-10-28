# Loops
# easy level
# Sum of N Natural Numbers: Write a Python program to calculate the sum of first N natural numbers using a loop.
num = int(input("Enter a natural number : "))
result = 0

if num > 0 :
    for i in range(1, num+1):
        result += i
else:
    print("Enter a valid natural number")
print(f"Sum of first {num} natural number is {result}")

# Factorial Calculator: Ask the user for a number and calculate its factorial using a for loop.
num1 = int(input("Enter a number to find factorial : "))
result_1 = 1
if num1 > 0:
    for i in range(1, num1 + 1):
        result_1 *= i
else:
    print("please enter a valid number.")
print(f"Factorial of {num1} is {result_1}")

# Multiplication Table Generator: Take a number from the user and print its multiplication table up to 10.
num2 = int(input("Enter a number to print a table : "))
print(f"Multiplication table for {num2} is:")
for i in range(1, 11):
    print(f"{num2} * {i} = {num2 * i}")

# Reverse a String: Input a string and reverse it using a loop (don’t use Python’s slicing).
input_str = input("Enter a string : ")
result_str = ""

if len(input_str) > 0:
    for i in input_str:
        result_str = i + result_str
else:
    print("Please enter a string")
print(f"Reverse of {input_str} is {result_str}")

# Count Even and Odd Numbers in a List: Given a list of integers, count how many are even and how many are odd using a loop.
list_1 = [1, 2, 3, 4, 5, 6, 7]
count_even = 0
count_odd = 0

for i in list_1:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(f"Number of even numbers in list {list_1} is {count_even}")
print(f"Number of odd numbers in list {list_1} is {count_odd}")

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

prime_int = int(input("Enter a number which you want find is prime or not : "))
if prime_int > 0:
    for i in range(2, prime_int):
        if prime_int % i == 0:
            print(f"{prime_int} is not a prime number.")
            break
        else:
            print(f"{prime_int} is a prime number.")
            break
else:
    print("Please enter a greater than 0.")

# Number Pattern Generator: Create this pattern using nested loops:

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print(" ")
    
# hard Level
# ATM Pin Attempts Simulation: Give the user 3 chances to enter the correct ATM PIN. If they fail all attempts, lock the account.
print("You have 3 attemepts to input correct pin so please give us correct pin and mind your attempt left")
pin_number = int(input("Enter your 4 - digit pin : "))
count_digit = 0
attempt = 1
corrected_pin = 1234


for i in range(0, len(str(pin_number))):
    count_digit += 1

if count_digit == 4:
    # print("you entered correct length of pin")
    while attempt < 3:
        if pin_number == corrected_pin:
            print("Welcome back Sir! How can i help you, today?")
            break
        else:
            print("Incorrect! Pin")
            attempt_left = 3 - attempt
            attempt += 1
            
            print(f"Attempt lefted : {attempt_left}")
            # print("Incorrect! Please enter your correct pin : ")
            pin_number = int(input("Please enter your correct pin : "))
        
        if attempt == 3:
            print("Attempt lefted : 0")
            print("Sorry your all attempts are over")
        
else:
    print("Please enter correct length of pin")

# Fibonacci Sequence Generator: Display the first N Fibonacci numbers using a while loop.
fib_num = int(input("Enter a number for generating first Fibonacci number: "))
i = 1
result_fib = 2
if fib_num > 0:
    print(f"So here is first {fib_num} Fiboacci numbers - ")
    print("1th - 1")
    while i < fib_num:
        print(f"{i + 1}th  - {result_fib}")
        result_fib = result_fib + i
        i += 1
else:
    print("Please enter a valid input of number to generate fibonacci series")