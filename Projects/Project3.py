# Email Slicer
import re
input_email = input("Enter your email : ")
if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', input_email):
    email_parts = input_email.split("@")
    print(f"UserName of input email {input_email} is {email_parts[0]}")
    email_subparts = email_parts[1].split(".")
    print(f"Domain of input email {input_email} is {email_parts[1]}")
    print(f"Provider of input email {input_email} is {email_subparts[0]}")
else:
    print("Please input correct email address.")