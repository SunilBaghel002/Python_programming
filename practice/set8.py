def greatestNumber(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greatest number")
    elif(b>a and b>c):
        print(f"{b} is greatest number")
    elif(c>a and c>b):
        print(f"{c} is greatest number")
    else:
        print("there is some mistake")

greatestNumber(6, 7, 4)

temp = int(input("Enter temperature : "))
def convertTemp(temp):
    res = (temp*9)/5 + 32
    return res
print(f"Conversion of {temp}°C in °F is", convertTemp(temp))

def calculateSum(num):
    if(num == 1):
        return 1
    else:
        return num + calculateSum(num - 1)
    
print(calculateSum(10))

def printPattern(n):
    for i in range(n, 0, -1):
        print("*" * i)
        
printPattern(3)

l1 = ["Sunil", "Baghel", "Mathura", "Haridwar", "Rishikesh", "Atulya"]

