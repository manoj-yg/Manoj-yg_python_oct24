# Input number of lines
side = int(input("Enter the side length for the hexagon: "))

for i in range(side):
    print(" " * (side - i) + "* " * side)
for i in range(side - 2, -1, -1):
    print(" " * (side - i) + "* " * side)
