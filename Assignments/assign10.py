# Input N
N = int(input("Enter the value of N: "))

# Define the sequence based on pattern observed
sequence = [1, 2, 2, 3, 3, 5, 5, 7, 8, 11, 13, 13]

# Print the Nth term if within sequence bounds
if N <= len(sequence):
    print(f"The {N}th term in the series is: {sequence[N-1]}")
else:
    print("The requested term is out of the sequence bounds.")
