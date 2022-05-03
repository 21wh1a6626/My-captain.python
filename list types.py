mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh "]
print(mylist)


mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh "]
print(len(mylist))


list1 = ["abc", 34, False , 40.9 , "male"]


mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh "]
print(type(mylist))


mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh "]
mylist[1] = "pooja"
print(mylist)


mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh "]
mylist[1:3] = ["pooja" , "ammu"]
print(mylist)



mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh "]
mylist.insert(2, "pooja")
print(mylist)


mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh "]
mylist.append("pooja")
print(mylist)



mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh "]
list2 = ["manu"]
mylist.extend(list2)
print(mylist)


mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh " , " Pooja "]
mylist.remove("anu")
print(mylist)



mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
mylist.pop(1)
print(mylist)


mylist = ["anu" ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
mylist.pop()
print(mylist)


mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
del mylist[0]
print(mylist)


mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
del mylist



mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
mylist.clear()
print(mylist)


mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
for i in range(len(

    mylist)):
  print(mylist[i])



mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1



mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
[print(x) for x in mylist]





mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
newlist = []

for x in mylist:
  if "a" in x:
    newlist.append(x)

print(newlist)



mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
mylist.sort()
print(mylist)


list = [100, 50, 65, 3, 56, 54, 45 , 23, 82, 23]
list.sort()
print(list)


list = [100, 50, 65, 3, 56, 54, 45 , 23, 82, 23]
list.sort(reverse = True)
print(list)



mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
mylist.sort()
print(mylist)


mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
mylist.sort(key = str.lower)
print(mylist)


mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
mylist.reverse()
print(mylist)



mylist = [" anu " ," harish" , " anjali " , " hasan " ," ritesh " , " pooja "]
list1 = mylist.copy()
print(list1)





list1 = ["1", "5", "8"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)



list1 = ["1", "5", "8"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)




list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)















