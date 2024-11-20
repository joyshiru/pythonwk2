#empty list
my_list = []


#append to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert 15 at the secnd position
my_list.insert(1, 15)

#extending the list
my_list.extend([50,60,70])

#remove last element from the list above
my_list.pop()

#sort in ascending order
my_list.sort()

#print the index of the value 30
#this is a set example
index_of_30 = my_list.index(30)

#The f in Python refers to an f-string, which is a way to format strings introduced in Python 3.6. It allows you to embed expressions inside string literals using curly braces {}.
print(f"The index of the value 30 is: {index_of_30}")

