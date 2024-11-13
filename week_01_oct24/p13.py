my_string = input("Enter a place name: ")
print(f"Type of '{my_string}' is {type(my_string)}")
for character in my_string:
    print(f"'{character}', Type = {type(character)}")
first_character = my_string[0]
print(f"First character = '{first_character}', Type = {type(first_character)}")
