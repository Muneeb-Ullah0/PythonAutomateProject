#list add
Thislist = ["apple", "banana", "cherry"]
Thislist.append("orange")
print(Thislist)

#list item change
Thislist = ["apple", "banana", "cherry"]
Thislist[1] = "blackcurrant"
print(Thislist)

#list remove
Thislist = ["apple", "banana", "cherry"]
Thislist.remove("banana")
print(Thislist)

#list loop
Thislist = ["apple", "banana", "cherry"]
if "grapes" in Thislist:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#copy lsit
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#clear all list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.clear()
print(mylist)

#pop list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.pop(1)
print(mylist)

#reverse list
thislist = ["apple", "banana", "cherry"]
thislist.reverse()
print(thislist)

#join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#list extend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

