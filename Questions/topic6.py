# Strings
# Easy level
# Count Vowels and Consonants: Write a Python program to count how many vowels and consonants are in a given string.
my_string = "hhaehjijsjflleiwa"
vowel_list = ["a", "e", "i", "o", "u"]
vowel_count = 0
consonant_count = 0
if len(my_string) > 0 :
    for i in vowel_list:
        if i in my_string:
            vowel_count = my_string.count(i)
            # print(i)
        else:
            consonant_count = my_string.count(i)
print(vowel_count, consonant_count)