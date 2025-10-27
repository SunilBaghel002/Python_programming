f= open("set2.py", "r")
text = f.read()         #only reads 4 characters
print(text)
text1 = f.readline()
# print(text1)

f.close()

new = open("hello.py", "w+")
setUp = new.write("Hi! there i am Sunil Baghel")
print(setUp)
new.close()