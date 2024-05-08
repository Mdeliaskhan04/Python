def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            print("Please enter a positive integer.")
        else:
            result = calculate_factorial(num)
            print(f"The factorial of {num} is {result}.")
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")
