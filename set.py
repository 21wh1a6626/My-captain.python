myset = {"c++", "html", "java"}
print(myset)

myset = {"c++", "html", "java" , "java"}
print(myset)

myset = {"c++", "html", "java" }
print(len(myset))


myset = {"c++", "html", "java" }
print(type(myset))


myset = {"c++", "html", "java" }
for x in myset:
  print(x)


myset = {"c++", "html", "java" }
print("html" in myset)


myset = {"c++", "html", "java" }
list = [ "python" , "javascript" ]
myset.update(myset)
print(myset)


myset = {"c++", "html", "java" }
myset.discard("html")
print(myset)

myset = {"c++", "html", "java" }
x = myset.pop()

print(x)
print(myset)


myset = {"c++", "html", "java" }
myset.clear()
print(myset)


myset = {"c++", "html", "java"}
for x in myset:
 print(x)


myset1 = {"c++", "html", "java" }
myset2 = { "python" , "javascript" }
set3 = myset1.union(myset2)
print(set3)


myset1 = {"c++", "html", "java" }
myset2 = { "python" , "javascript" }
myset1.update(myset2)
print(myset1)


myset1 = {"c++", "html", "java" }
myset2 = { "python" , "javascript" }
myset1.intersection_update(myset2)
print(myset1)

myset1 = {"c++", "html", "java" }
myset2 = { "python" , "javascript" }
set3 = myset1.intersection(myset2)
print(set3)


myset1 = {"c++", "html", "java" }
myset2 = { "python" , "javascript" }
myset1.symmetric_difference_update(myset2)

print(myset1)


myset1 = {"c++", "html", "java" }
myset2 = { "python" , "javascript" }
set3 = myset1.symmetric_difference(myset2)

print(set3)
