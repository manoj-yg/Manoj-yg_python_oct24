lines = int(input("Enter the number of lines for the triangle: "))

for i in range(1, lines + 1):
    if i == 1:
        print(" " * (lines - i) + "*")
    elif i == lines:
        print("* " * i)
    else:
        print(" " * (lines - i) + "*" + " " * (2 * i - 3) + "*")
