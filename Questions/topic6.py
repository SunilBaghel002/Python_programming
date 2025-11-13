# Strings
# Easy level
# Count Vowels and Consonants: Write a Python program to count how many vowels and consonants are in a given string.
my_string = input("Enter a string : ")

vowel_list = ["a", "e", "i", "o", "u"]
vowel_count = 0
consonant_count = 0

if len(my_string) > 0 and my_string.isalpha():
    for i in vowel_list:
        if i in my_string:
            vowel_count += my_string.count(i)
            
    consonant_count = len(my_string.lower()) - vowel_count
    print(F"In this string, {my_string} there are {vowel_count} vowels and {consonant_count} consonants.")
    
else:
    print("Please enter a valid string")

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
from collections import Counter

my_string = "programming"
counts = Counter(my_string)
duplicate_chars = [char for char, count in counts.items() if count > 1]

duplicate_string = ''
for i in duplicate_chars:
    duplicate_string += i
    my_string = my_string.replace(duplicate_string, "")

print(f"Output String by removing these duplicate character {duplicate_string} is {my_string}")

# Character Frequency Counter: Input a string and display each character’s frequency (ignore case). Example: "Mississippi" → {'m':1, 'i':4, 's':4, 'p':2}
frequency_str = "Mississippi"
frequency_str = frequency_str.lower()
frequency_counts = Counter(frequency_str)

print(f"Hence, count of characters in {frequency_str} is {frequency_counts}")

# Find the Longest Word in a Sentence Example: Input: "Python makes programming fun", Output: "programming"
word_str = "Python makes programming fun"
spilt_word_str = word_str.split(" ")
print(f"Hence the longest word in {word_str} is {max(spilt_word_str)}")

# Hard Level
# Word Occurrence Counter (Ignore Case, Remove Punctuation): Count how many times each word appears in a paragraph — ignoring case and punctuation.
paragraph = "Python makes programming fun fun fun makes"
spilt_paragraph = paragraph.split(" ")
paragraph_counts = Counter(spilt_paragraph)
print(paragraph_counts)

# String Compression (Run-Length Encoding) Example: Input: "aaabbccddd", Output: "a3b2c2d3"
orginal_str = "aaabbccddd"
encoded_string = []
count = 1
    
for i in range(1, len(orginal_str)):
    if orginal_str[i] == orginal_str[i-1]:
            count += 1
    else:
        encoded_string.append(orginal_str[i-1])
        if count > 1:  
            encoded_string.append(str(count))
        count = 1
    
encoded_string.append(orginal_str[-1])
if count > 1:
    encoded_string.append(str(count))
    
compressed_str = ''
for i in encoded_string:
    compressed_str += i
print(compressed_str)