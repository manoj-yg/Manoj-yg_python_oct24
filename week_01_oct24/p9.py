input_number = int(input("Enter a number to find your lucky digit: "))
sum_of_digits = 0
while input_number >= 10:
    sum_of_digits = 0
    while input_number > 0:
        sum_of_digits += input_number % 10
        input_number //= 10
    input_number = sum_of_digits
print(f"Your lucky digit is {sum_of_digits}")
