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

