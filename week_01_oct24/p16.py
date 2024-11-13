my_str = 'bengaluru'

print(my_str[:])        # Prints the whole string: 'bengaluru'
print(my_str[::])       # Also prints the whole string: 'bengaluru'
print(my_str[1:8])      # Prints from index 1 to 7: 'engalur'
print(my_str[2:6:2])    # Prints every 2nd character from index 2 to 5: 'na'
print(my_str[::2])      # Prints every 2nd character of the whole string: 'bnauu'
print(my_str[::-2])     # Prints every 2nd character in reverse: 'uuanb'
print(my_str[::-1])     # Prints the entire string in reverse: 'urulagneb'
