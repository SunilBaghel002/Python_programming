i = 1
while i<=50:
    print(i)
    i=i+1

content_list = [1, 2, 3, "Sunil", "Baghel", "SDE"]
i=0
while i<len(content_list):
    print(content_list[i])
    i=i+1
    
for items in content_list:
    print(items)
    
for j in range(0, 10, 3):
    print(j)
    
rows = 5
for k in range(1, rows):
    print(" " * (rows-k) + "*" * (2*k-1))
for k in range(rows,0,-1):
    print(" " * (rows-k) + "*" * (2*k-1))
    
for k in range(1, rows):
    for l in range(1, k+1):
        print(l, end=" ")
    print()
    
print("  ")
    
for k in range(rows):
    for l in range(rows):
        if k == 0 or k == rows - 1 or l == 0 or l == rows -1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()