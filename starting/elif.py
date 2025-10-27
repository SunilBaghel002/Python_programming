age = int(input("Enter your age : "))
if(age>18 and age<100):
    print("yes")
elif(age<0 or age>100):
    print("enter a valid age")
else:
    print("no")