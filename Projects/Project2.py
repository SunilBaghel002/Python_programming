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