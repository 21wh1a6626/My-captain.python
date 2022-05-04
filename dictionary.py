dict = {1: "c++", 2: "java" , 3: "python"}
print("\nDictionary with Keys and values : ")
print(dict)

dict = {1: "c++", 2: "java" , 3: "python"}
print(dict[3])

dict = {1: "c++", 2: "java" , 3: "python" , 3: "python"}
print(dict)

dict = {1: "c++", 2: "java" , 3: "python"}
print(len(dict))

dict = {1: "c++", 2: "java" , 3: "python"}
x = dict.get('c++')
print(x)


dict = {1: "c++", 2: "java" , 3: "python"}
x = dict.keys()


dict = {1: "c++", 2: "java" , 3: "python"}
x = dict.keys()
print(x) 

dict[4] = "html"
print(x)


dict = {1: "c++", 2: "java" , 3: "python"}
x = dict.values()
print(x)

dict[3] = "html"
print(x)


dict = {1: "c++", 2: "java" , 3: "python"}
if "3" in dict:
  print("Yes, '3' is one of the keys in the dict dictionary")



dict = {1: "c++", 2: "java" , 3: "python"}
dict["3"] = "html"


dict = {1: "c++", 2: "java" , 3: "python"}
dict.update({"2": "html"})


dict = {1: "c++", 2: "java" , 3: "python"}
dict["4"] = "html"
print(dict)

dict = {1: "c++", 2: "java" , 3: "python"}
dict.pop(2)
print(dict)

dict = {1: "c++", 2: "java" , 3: "python"}
dict.popitem()
print(dict)

dict = {1: "c++", 2: "java" , 3: "python"}
del dict[2]
print(dict)


dict = {1: "c++", 2: "java" , 3: "python"}
del dict
print(dict)


dict = {1: "c++", 2: "java" , 3: "python"}
dict.clear()
print(dict)

dict = {1: "c++", 2: "java" , 3: "python"}
for x in dict:
  print(x)

dict = {1: "c++", 2: "java" , 3: "python"}
for x in dict:
  print(dict[x])

dict = {1: "c++", 2: "java" , 3: "python"}
for x in dict.values():
  print(x)


dict = {1: "c++", 2: "java" , 3: "python"}
for x in dict.keys():
  print(x)


dict = {1: "c++", 2: "java" , 3: "python"}
for x, y in dict.items():
  print(x, y)


dict = {1: "c++", 2: "java" , 3: "python"}
mydict = dict.copy()
print(mydict)


myfriends = {
  "friend1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "friend2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "friend3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
