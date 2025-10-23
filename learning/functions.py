#1-reusability
#2-modularity
#3-scoping

def greet(name):
    print(f"Hi, {name}")
    
greet("Sunil")

def get_full_name(first_name, last_name):
    full_name = first_name + last_name
    return full_name
name = get_full_name("sunil", "baghel")
print(name)

def my_deco(func):
    def wrapper():
        print("hhjhjkjkhejfhub")
        func()
        print("diwwwosicinddddd")
    return wrapper
@my_deco
def say_hello():
    print("hello")
say_hello()

def count_down(num):
    while num>-10:
        yield num
        num -=1

print(count_down(5))

for number in count_down(5):
    print(number)
    
add_ten = lambda x: x+10
print(add_ten(5))