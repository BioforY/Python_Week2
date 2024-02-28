#Create an empty list:
my_list=[]
#Append elements to the list:
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#Insert value at the second position in the list:
my_list.insert(1, 15)
print(my_list)
#Extend list with another list:
list2=[50, 60, 70]
my_list.extend(list2)
print(my_list)
#Remove the last element from my list:
my_list.remove(70)
print(my_list)
#Sort my list in an ascending order:
my_list.sort()
print(my_list)
#Find and print the index of the value 30 in my list:
index=my_list.index(30)
print(index)