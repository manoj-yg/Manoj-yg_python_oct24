my_str = "banashankari"
print("Index of 's':", my_str.find('s'))           # Should return 4
print("Index of 'shankari':", my_str.find('shankari'))  # Should return 4
print("Index of 'a' after position 3:", my_str.find('a', 3)) # Should return 3
try:
    print("Index of 'm':", my_str.index('m'))  # This will raise a ValueError
except ValueError:
    print("'m' is not found in the string.")
