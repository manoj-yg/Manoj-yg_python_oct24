#Find Sum of the First and Last Digits of a Number
# Input number
number = input("Enter a number: ")

# Calculate the sum of first and last digit
first_digit = int(number[0])
last_digit = int(number[-1])

print(f"The sum of the first and last digits is: {first_digit + last_digit}")
