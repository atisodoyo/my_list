my_list= list()
numbers= (10,20,30,40)
my_list.extend(numbers)
#print(my_list)
my_list.insert(1,15)
my_list.extend(50,60,70)
#print(my_list)
#remove the last element from the list
last_element= my_list.pop()
print(my_list)
#output: (10,15,20,30,40,50,60)
print (last_element)
#output: 'python'
#sort the list in ascending order
my_list.sort(10,15,20,30,40,50,60)
#print the sorted list
print(my_list)
#find and print the index of the value 30 in my_list
index_of_thirty=my_list.index(30)
#print the index of the value of 30
print("The index of the value 30 in my_list is:", index_of_thirty)