# # Email Slicer
# import re
# input_email = input("Enter your email : ")
# if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', input_email):
#     email_parts = input_email.split("@")
#     print(f"UserName of input email {input_email} is {email_parts[0]}")
#     email_subparts = email_parts[1].split(".")
#     print(f"Domain of input email {input_email} is {email_parts[1]}")
#     print(f"Provider of input email {input_email} is {email_subparts[0]}")
# else:
#     print("Please input correct email address.")

# # Password Strength Checker
# input_password = input("Enter a password : ")
# print(f"Length of password is {len(input_password)}")

# count_upper = count_lower = count_numbers = count_special = 0

# if len(input_password) > 7 :
#     for ch in input_password:
#         if ch.isupper():
#             count_upper += 1
#         elif ch.islower():
#             count_lower += 1
#         elif ch.isnumeric():
#             count_numbers += 1
#         else:
#             count_special += 1
            
#     if 0 in (count_special, count_lower, count_numbers, count_upper):
#         print("Password status is easy")
        
#     elif count_upper> 0 and count_lower > 0 and count_numbers > 0 and count_special > 0:
#         print("Password is Strong!!")
        
#     else:
#         print("Password strength is medium")
        
#     print(f'''
#     Count of 
#         Capital Alphabets - {count_upper}
#         Small Albhabets - {count_lower}
#         Numbers - {count_numbers}
#         Special - {count_special}
#           ''')
    
# else:
#     print("Please enter password of length greater than 7")
    
# Word & Character Analyzer Tool
import re
from collections import Counter

paragraph = "Hey! i am sunil a btech student hey"
characters = paragraph.replace(" ", "")

print(f"Total characters in {paragraph} is : {len(characters)}")

words = re.findall(r'\b\w+\b', paragraph.lower())
print(f"Total words in {paragraph} is {len(words)}")

unique_words = set(words)
print(f"Unique words are {unique_words} and length of unique words are {len(unique_words)}")

counts = Counter(words)

most_common_word = counts.most_common(1)
print(f"The most common word is: '{most_common_word[0][0]}' (repeated {most_common_word[0][1]} times)")

total_length = paragraph.split(" ")

average_length = len(characters)/len(total_length) 
print(f"Average word length is {average_length}")
