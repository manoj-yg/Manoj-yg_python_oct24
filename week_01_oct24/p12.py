input_number = int(input("Enter a number to find the frequency of a specific digit: "))
target_digit = int(input("Enter the digit whose frequency you want to find: "))
frequency = 0
temp_number = input_number
while temp_number > 0:
    digit = temp_number % 10
    if digit == target_digit:
        frequency += 1
    temp_number //= 10
print(f"Frequency of {target_digit} is:", frequency)