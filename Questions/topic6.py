# # Strings
# # Easy level
# # Count Vowels and Consonants: Write a Python program to count how many vowels and consonants are in a given string.
# my_string = input("Enter a string : ")

# vowel_list = ["a", "e", "i", "o", "u"]
# vowel_count = 0
# consonant_count = 0

# if len(my_string) > 0 and my_string.isalpha():
#     for i in vowel_list:
#         if i in my_string:
#             vowel_count += my_string.count(i)
            
#     consonant_count = len(my_string.lower()) - vowel_count
#     print(F"In this string, {my_string} there are {vowel_count} vowels and {consonant_count} consonants.")
    
# else:
#     print("Please enter a valid string")

# Reverse a String Without Using [::-1]: Take a string input from the user and reverse it manually using loops.
input_str = input("Enter a string : ")
result_str = ""

if len(input_str) > 0:
    for i in input_str:
        result_str = i + result_str
    print(f"Reverse of {input_str} is {result_str}.")
else:
    print("Enter a valid string.")

# Check Palindrome: Write a program that checks if a string is a palindrome (e.g., “madam”, “racecar”).
palindrome_str = input("Enter a string : ")
reversed_str = palindrome_str[::-1]
if len(palindrome_str) > 0 :
    if palindrome_str == reversed_str :
        print(f"{palindrome_str} is a Palindrome string.")
    else:
        print(f"{palindrome_str} is a Normal string.")
else:
    print("Please enter a valid string.")

# Moderate Level
# Remove Duplicates from a String: Input: "programming" → Output: "progamin"
normal_str = "programming"
normal_str.