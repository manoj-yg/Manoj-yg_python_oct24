n = int(input("Enter the value of n: "))

# Initialize sum
series_sum = 0
# Calculate the sum of the series up to 10 terms
for i in range(1, 11):
    series_sum += n ** i

print(f"Sum of the series (n + n^2 + ... + n^10) is: {series_sum}")
