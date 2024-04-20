print("WELCOME TO GANESH DIAMOND PATTERN-->")
def print_diamond(n):
    # THE TOP OF DIAMOND
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    
    # THE BOTTOM OF DIAMOND
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# WRITTEN FOR USER INPUT
try:
    n = int(input("Enter the number of rows: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print_diamond(n)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
