# conditional statements

# 1. Temperature Converter with Category Classification
# Problem: Convert temperature between Celsius, Fahrenheit, and Kelvin — also tell whether it’s freezing, moderate, or hot.

input_celsius = float(input("Enter a celsius value which you want to convert to fahrenheit and kelvin : "))

result = (9*input_celsius)/5 + 32
result_1 = input_celsius + 273

print(f"Coversion of {input_celsius}°C is {result}°F")
print(f"Coversion of {input_celsius}°C is {result_1} Kelvin")

if input_celsius < 0:
    print("It's freezing cold!")
elif 0 <= input_celsius <= 25:
    print("Weather is moderate.")
else:
    print("It's hot today!")
    
# 2. ATM Cash Withdrawal Simulator
# Problem: Simulate ATM withdrawal — check for sufficient balance, daily limits, and ATM cash availability.
balance = 10000
daily_limit = 15000
atm_cash = 8000
amount = int(input("Enter amount to cash you want to withdraw : "))

if amount > 0:
    if amount > balance:
        print("Insufficient balance")
    elif amount > daily_limit:
        print("Daily limit exceeded")
    elif amount > atm_cash:
        print("Sorry, but bank don't have enough cash available.")
    else:
        print(f"Transaction successful - {amount} is withdraw from bank")
        balance = balance - amount
        print(f"Net Balance - {balance}")
else:
    print("Please enter a valid amount of cash")

# 3. Discount Calculator for Online Store
#Problem: A store gives different discounts based on purchase amount.
bill = float(input("Enter your total bill: "))

if bill > 0:
    if bill >= 5000:
        discount = bill * 0.20
    elif bill >= 1000:
        discount = bill * 0.10
    else:
        discount = 0
else:
    print("Please enter a vaild bill")
    
print(f"Final Bill: ₹{bill - discount}")

# 4. Basic Login System
# Problem: Ask username and password, validate using stored values.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login successful!")
else:
    print("Invalid credentials.")

# Intermediate
# 5. Electricity Bill Calculator
# Problem: Calculate monthly electricity bill based on units consumed.
units_consumed = int(input("Enter unit consumed : "))
if units_consumed >= 0:
    if units_consumed >= 0 and units_consumed <= 100:
        price_per_unit = 5
    elif units_consumed > 100 and units_consumed <= 200:
        price_per_unit = 7
    else:
        price_per_unit = 10
else:
    print("Enter valid units.")

net_electricity_bill = units_consumed * price_per_unit
print(f"Net Electricity Bill : {net_electricity_bill}")

# 6. Bus Ticket Fare System
# Problem: Different fares for children, adults, and senior citizens.
age = int(input("Enter age: "))
distance = float(input("Enter distance in km: "))

if age >= 0 and distance >= 0:
    if age < 12:
        fare = distance * 2
    elif age >= 60:
        fare = distance * 3  # discounted
    else:
        fare = distance * 5
else:
    print("Please enter a valid age and distance to calculate fare.")

print(f"Total fare: ₹{fare}")

# 7. BMI (Body Mass Index) Health Checker
# Problem: Take height and weight and tell if user is underweight, normal, or overweight.
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)

if weight >=0 and height >= 0:
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    elif 25 <= bmi < 30:
        print("Overweight")
    else:
        print("Obese")
else:
    print("Please enter a vaild weight and height")

# Advanced
# 8. Smart Traffic Light System (Simulation)
# Problem: Simulate traffic lights based on traffic density (low, medium, high).
traffic_density = int(input("Enter density of traffic : "))
if traffic_density >= 0:
    if traffic_density >= 0 and traffic_density <= 30:
        signal_priority = "Green"
        signal_duration = 10
    elif traffic_density > 30 and traffic_density <= 60:
        signal_priority = "Yellow"
        signal_duration = 20
    elif traffic_density > 60 and traffic_density <= 100:
        signal_priority = "Red"
        signal_duration = 30
    else:
        print("Traffic percentage is high than 100%.")
else:
    print("Please enter a valid percentage of traffic.")

print(f"On the basis of {traffic_density} signal-priority is \n {signal_priority} and \n signal-duration is {signal_duration}")

