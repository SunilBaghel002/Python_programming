num1 = int(input("enter a number : "))
for i in range(1, 11):
    print(f"{num1} * {i} is",num1*i)
    
l1 = ["Sunil", "Satyam", "Aryan", "Anuj", "Dev"]

for names in l1:
    if(names.startswith("S")):
        print(f"Good Morning, {names}")
    elif(names.startswith("A")):
        print(f"Hey there! {names}")
    # print(names)

i = 1
while i<=10:
    print(f"{num1} * {i} is",num1*i)
    i = i+1

if num1>1:
    for i in range(2, num1):
        if(num1%i == 0):
            print("it is not a prime number")
            break
        else:
            print("Number is prime")
            break
else:
    print("enter a valid number")

res = 0
for i in range(1, num1+1):
    res = res + i
print(f"Sum of first {num1} natural numbers is", res)

i = 0
res = 0
while i<=num1:
    res = res + i
    i = i +1
print(f"Sum of first {num1} natural numbers is", res)

res = 1
for i in range(1, num1+1):
    res = res*i
print(f"Factorial of {num1} is", res)

rows = 3
for i in range(0, rows+1):
    print(" " * (rows-i) + "*" * (2*i-1))
    
print(" ")

for i in range(1, rows+1):
    print("*" * i)
    
print(" ")

for i in range(rows):
    for j in range(rows):
        if(i  ==0 or  i == rows-1 or j == 0 or j == rows - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")

for i in range(10, 0, -1):
    print(f"{num1} * {i} is",num1*i)