# Function to calculate binomial coefficient
#pascal triangle
def binomial_coeff(n, k):
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

# Input number of lines
lines = int(input("Enter the number of lines for Pascal's Triangle: "))

for i in range(lines):
    print(" " * (lines - i), end="")
    for j in range(i + 1):
        print(binomial_coeff(i, j), end=" ")
    print()
