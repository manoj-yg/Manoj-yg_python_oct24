# Function to check if a digit is prime
def is_digit_prime(digit):
    return digit in {2, 3, 5, 7}

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input number
number = int(input("Enter a number: "))

# Calculate the sum of prime digits
sum_prime_digits = sum(int(digit) for digit in str(number) if is_digit_prime(int(digit)))

# Check if the sum is prime
if is_prime(sum_prime_digits):
    print(f"The sum of prime digits ({sum_prime_digits}) is a prime number.")
else:
    print(f"The sum of prime digits ({sum_prime_digits}) is not a prime number.")
