input_number = int(input("Enter a number to find the sum of its digits: "))
sum_of_digits = 0
while input_number > 0:
    sum_of_digits += input_number % 10
    input_number //= 10
print(f"Sum of digits is {sum_of_digits}")
