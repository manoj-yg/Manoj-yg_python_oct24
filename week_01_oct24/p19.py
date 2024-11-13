my_str = 'banashankari'
sub_string = 'm'

try:
    print(my_str.index('s'))  # 4
    print(my_str.index(sub_string))  # Will raise ValueError because 'm' is not found
    print(my_str.index('shankari'))  # 4
except ValueError as e:
    print(f'The substring "{sub_string}" not found')
    print(e)
except Exception as e:
    print(f'Some error occurred: {e}')
