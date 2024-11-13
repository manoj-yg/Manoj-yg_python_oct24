# Input side length (odd number for symmetry)
size = int(input("Enter an odd number for the side length of the X shape: "))

for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
