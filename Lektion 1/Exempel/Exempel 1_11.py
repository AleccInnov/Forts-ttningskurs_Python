# listor ta bort

my_list = [1, 2, 3, "hello", 4.5, 3]

print("Orörd lista ")
print(my_list)

#my_list.remove(3)  # Removes the first occurrence of the value 3

#print("Första 3:an raderad ")
#print(my_list)

#del my_list[0]
#print("Index 0 raderad ")
#print(my_list)

popped_value = my_list.pop(2)  # Removes and returns the element at index 2
print("Index 2 borttagen och returnerad ")
print(my_list)

print("Index 2")
print(popped_value)

my_list.insert(2, popped_value)  # Insert 3 (popped_value) i index 2
print(my_list)


