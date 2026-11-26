#List append
list = [3, 7, 20, 'Tech IS', 'Make me learn fun']
print(list)
list.append('one')
print(list)
list.extend(["let's", "make", "this", "happen"])
print(list)
list.insert(3, "Chocolate")#Inserting chocolate in index 3
print(list)
list.remove(20)#Remove 20 from list
print(list)
#Extend used to add multiple elements at the end of the list.
list.pop(1)#pop index 1 from list
print(list)
#Remove() - removes element from identification
#Pop() - removes element using index
#List slicing - Used to extract sub section of the list
new_list = [3, 7, 20, '@', 'Tech IS','Make me learn fun']
print(new_list[:4])
print(new_list[2:])
print(new_list[1:5])
print(new_list[:])