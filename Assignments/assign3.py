def is_alphanumeric(char):
    return char.isalnum()

char =input("Enter the alphanumeric number:  ")
if is_alphanumeric(char):
    print(f"'{char}' is alphanumeric.")
else:
    print(f"'{char}' is not alphanumeric.")
