input_number = int(input('Enter a number to find your lucky digit: '))

sum_of_digits = 0
temp_number = input_number

while temp_number>=0:
    remainder_digit = temp_number%10
    temp_number = temp_number//10
    sum_of_digits += remainder_digit