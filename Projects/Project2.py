# Number Guessing Game - Program keeps asking for guesses until the correct number is guessed.
# guess_num = int(input("Enter a number : "))
correct_num = 10
attempt=5
while attempt >= 0:
    guess_num = int(input("Enter a number : "))
    if guess_num == correct_num:
        print("You guessed it right!! You Won!!")
        break
    else:
        print("You lost! Try again.")
        print(f"Your attempt left - {attempt}")
        attempt -= 1

# Billing System for Small Shop: Continuously take item prices until user enters 0, then show total and average.

item_names = []
item_prices = []

while True:
    item_input = input("Enter item name and price in this form Item_name-Item_price : ")

    if item_input == "0":
        print("Ok, now your store is ready")
        break

    name, price = item_input.split("-")
    item_names.append(name)
    item_prices.append(float(price))

total = sum(item_prices)
bil_avg = total/len(item_prices)
print(f"Total Bill - {total}")
print(f"Average of bill : {bil_avg}")

# Countdown Timer - User enters seconds → countdown prints every second
import time

user_input_time = input("Enter time in second : ")

if user_input_time.isdigit():
    time_number = int(user_input_time)
    
    print(f"You just created {time_number} second countdown timer")
    print("CountDown started: ")
    
    for i in range(1, time_number+1):
        time.sleep(i)
        j = str(i)
        print(j+"."*i)    
              
else:
    print("Please enter number")

# Banking Menu System - Repeatedly show options (Deposit, Withdraw, Exit). Exit only when user chooses.
print("Welcome to ABC Bank, Tell us how can we help you today!")

while True:
    print('''
Input a number based on your request
    1 - Deposit
    2 - Withdraw
    3 - Help
    4 - Exit
''')
    
    user_bank_input = input("Enter a number based on your request : ")
    
    if user_bank_input.isdigit():
        user_bank_number = int(user_bank_input)
        
        if user_bank_number == 4:
            print("Thanks for visiting our bank.")
            break
        
        elif user_bank_number == 1:
            print("Your request is Deposit")
            
        elif user_bank_number == 2:
            print("Your request is Withdraw")
            
        elif user_bank_number == 3:
            print("Your request is Help")
            
        else:
            print("Invalid request")
    else:
        print("Please enter a number.")
        
# Password Strength Validator - Loop through characters to count uppercase, lowercase, digits, symbols.
def password_strength_validator(pw: str):
    """
    Count uppercase, lowercase, digits and symbols in pw.
    Return: (status, count_upper, count_lower, count_digit, count_symbol)
    status is "easy" if any of the 4 categories is 0, otherwise "hard".
    """
    count_upper = count_lower = count_digit = count_symbol = 0

    for ch in pw:
        if ch.isupper():
            count_upper += 1
        elif ch.islower():
            count_lower += 1
        elif ch.isdigit():
            count_digit += 1
        else:
            count_symbol += 1

    if 0 in (count_upper, count_lower, count_digit, count_symbol):
        status = "easy"
    else:
        status = "hard"

    return status, count_upper, count_lower, count_digit, count_symbol


new_password = input("Enter a new password : ")

status, count_upper, count_lower, count_digit, count_symbol = password_strength_validator(new_password)

print(f"Status: {status}")
print(f"Upper: {count_upper}, Lower: {count_lower}, Digits: {count_digit}, Symbols: {count_symbol}")

while status == "easy":
    print("Password is too weak. It must include at least one uppercase, lowercase, digit and symbol.")
    new_password = input("Enter a new password : ")
    status, count_upper, count_lower, count_digit, count_symbol = password_strength_validator(new_password)

print(f"Final password accepted as {new_password}")
