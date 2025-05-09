# Flyttal formateras med två decimaler
float_number = 123.456789
formatted_float = "Flyttal: {:.2f}".format(float_number)

# Sträng formateras med en viss bredd och är vänsterjusterad
string_value = "Python"
formatted_string_left = "{:<10}Sträng (vänsterjusterad): ".format(string_value)

# Sträng formateras med en viss bredd och är centrerad
formatted_string_center = "{:^10}Sträng (centrerad): ".format(string_value)

# Heltal formateras med en viss bredd och är högerjusterad
integer_number = 42
formatted_integer = "{:10d}Heltal (högerjusterad): ".format(integer_number)

# Skriv ut de formaterade strängarna
print(formatted_float)
print(formatted_string_left)
print(formatted_string_center)
print(formatted_integer)
