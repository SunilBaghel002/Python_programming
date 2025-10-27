d1 = {
    "name" : "Sunil",
    "class" : "5th Sem Cse",
    "role" : "Full stack developer"
}

print(d1, type(d1))
print(d1["class"])
print(d1.keys())
print(d1.values())

d2 = {}
print(d2)    #empty dict

s1 = set() #an empty set

print(s1, type(s1))

s2 = {1, 2, 3, 4, 45}
s3 = {45, 2, 3}
print(s2)
print(s2.union(s3))
print(s2.issuperset(s3))
print(s2.isdisjoint(s3), s2.difference(s3), s2.clear())
print(s2)