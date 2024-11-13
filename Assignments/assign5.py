# Input the values of n and M
n = int(input("Enter the value of n: "))
M = int(input("Enter the number of terms (M): "))

# Initialize sum
series_sum = 0

# Calculate the sum with alternating signs
for i in range(M):
    term = (-n) ** i  # Alternates sign by raising -n to power i
    series_sum += term

print(f"Sum of the series (1 - n + n^2 - ... up to {M} terms) is: {series_sum}")
#Find Sum of the Series: 