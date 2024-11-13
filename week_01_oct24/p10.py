input_number = int(input("Enter a number to find the biggest and smallest digits: "))
biggest_digit = -1
smallest_digit = 10
temp_number = input_number
while temp_number > 0:
    digit = temp_number % 10
    if digit > biggest_digit:
        biggest_digit = digit
    if digit < smallest_digit:
        smallest_digit = digit
    temp_number //= 10
print("Biggest digit is:", biggest_digit)
print("Smallest digit is:", smallest_digit)
