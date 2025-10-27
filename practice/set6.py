a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
d = int(input("enter fourth number : "))

if(a>b and a>c and a>d):
    print(a,"is the greatest number among these")
elif(b>a and b>c and b>d):
    print(b,"is the greatest number among these")
elif(c>a and c>b and c>d):
    print(c,"is the greatest number among these")
elif(d>a and d>b and d>c):
    print(d,"is the greatest number among these")
else:
    print("there is some mistake in number please check it")

marks1 = int(input("enter marks of first subject"))
marks2 = int(input("enter marks of second subject"))
marks3 = int(input("enter marks of third subject"))

avg = (marks1 + marks2 + marks3)/3

if(avg>=33 and avg<40):
    print("Your pass")
elif(avg>=40 and avg<100):
    print("You scrore good marks")
elif(avg>0 and avg<33):
    print("you are fail")
else:
    print("Enter valid marks")

name = input("Enter a name : ")
if(len(name)>=10):
    print(name,"it contains of 10 characters")
else:
    print("No it don't have that much characters")

spam_list = ["make a lot of money", "click this", "buy now", "subscribe now"]
message = "click this"

if message in spam_list:
    print(f"Alert! {message} this is a spam message")
else:
    print("It's is safe")

articles = "Hello, Everyone my name is Sunil and i am a beginner in python."
name = "Sunil"
if name in articles:
    print("Yes, this article is talking about Sunil")
else:
    print("Nope!")