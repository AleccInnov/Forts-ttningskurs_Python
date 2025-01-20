# sortera en lista

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(my_list)

# sortera-funktionen som ändrar i my_list
my_list.sort(reverse=True)  # reverse=True
print(my_list)

# sortera-funktionen som sorterar till en ny list-variabel utan att ändra my_list
sorted_list = sorted(my_list)
print(sorted_list)


