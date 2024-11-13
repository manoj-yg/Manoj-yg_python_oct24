# Input the values of n and m
n = float(input("Enter the value of n (1 < n < 5): "))
m = int(input("Enter the number of terms (1 < m < 10): "))

# Initialize sum
series_sum = 1  # Starts from 1
exponent = 1
denominator = 3

# Calculate the sum with increasing exponents and denominators
for i in range(1, m):
    term = (n ** exponent) / denominator
    if i % 2 == 1:
        series_sum -= term
    else:
        series_sum += term
    exponent *= 2
    denominator += 2

print(f"Sum of the series is: {series_sum}")
