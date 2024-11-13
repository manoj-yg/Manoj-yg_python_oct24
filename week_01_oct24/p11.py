input_number = int(input("Enter a number to find the sum of even and odd digits: "))
sum_even = 0
sum_odd = 0
temp_number = input_number
while temp_number > 0:
    digit = temp_number % 10
    if digit % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit
    temp_number //= 10
print("Sum of even digits is:", sum_even)
print("Sum of odd digits is:", sum_odd)