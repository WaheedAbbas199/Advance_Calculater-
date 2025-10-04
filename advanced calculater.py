import math

# Global history list
history = []

def add(x, y):
    result = x + y
    history.append(f"{x} + {y} = {result}")
    return result

def subtract(x, y):
    result = x - y
    history.append(f"{x} - {y} = {result}")
    return result

def multiply(x, y):
    result = x * y
    history.append(f"{x} * {y} = {result}")
    return result

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    result = x / y
    history.append(f"{x} / {y} = {result}")
    return result

def exponent(x, y):
    result = x ** y
    history.append(f"{x} ^ {y} = {result}")
    return result

def square_root(x):
    if x < 0:
        return "Error! Negative number."
    result = math.sqrt(x)
    history.append(f"√{x} = {result}")
    return result

def modulus(x, y):
    result = x % y
    history.append(f"{x} % {y} = {result}")
    return result

def factorial(x):
    if x < 0:
        return "Error! Negative number."
    result = math.factorial(x)
    history.append(f"{x}! = {result}")
    return result

def percentage(x, y):
    result = (x / 100) * y
    history.append(f"{x}% of {y} = {result}")
    return result

def gcd_lcm(x, y):
    gcd_val = math.gcd(x, y)
    lcm_val = math.lcm(x, y)
    history.append(f"GCD({x},{y}) = {gcd_val}, LCM({x},{y}) = {lcm_val}")
    return gcd_val, lcm_val

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def number_conversion(n):
    return bin(n), oct(n), hex(n)

def multiplication_table(n):
    table = [f"{n} x {i} = {n*i}" for i in range(1, 11)]
    return table

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

def view_history():
    return history if history else ["No history available."]

def clear_history():
    history.clear()
    return "History cleared successfully!"

# ---------------- Main Program ----------------
while True:
    print("\n--- Advanced Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Modulus")
    print("8. Factorial")
    print("9. Percentage")
    print("10. GCD / LCM")
    print("11. Prime Check")
    print("12. Even/Odd Check")
    print("13. Number Conversion (Binary/Octal/Hex)")
    print("14. Multiplication Table")
    print("15. Sum of Digits")
    print("16. Reverse of Number")
    print("17. Calculation History")
    print("18. Clear History")
    print("19. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        x, y = map(float, input("Enter two numbers: ").split())
        print("Result:", add(x, y))

    elif choice == "2":
        x, y = map(float, input("Enter two numbers: ").split())
        print("Result:", subtract(x, y))

    elif choice == "3":
        x, y = map(float, input("Enter two numbers: ").split())
        print("Result:", multiply(x, y))

    elif choice == "4":
        x, y = map(float, input("Enter two numbers: ").split())
        print("Result:", divide(x, y))

    elif choice == "5":
        x, y = map(float, input("Enter base and exponent: ").split())
        print("Result:", exponent(x, y))

    elif choice == "6":
        x = float(input("Enter a number: "))
        print("Result:", square_root(x))

    elif choice == "7":
        x, y = map(int, input("Enter two integers: ").split())
        print("Result:", modulus(x, y))

    elif choice == "8":
        x = int(input("Enter a number: "))
        print("Result:", factorial(x))

    elif choice == "9":
        x, y = map(float, input("Enter percentage and number (e.g., 20 150): ").split())
        print("Result:", percentage(x, y))

    elif choice == "10":
        x, y = map(int, input("Enter two integers: ").split())
        gcd_val, lcm_val = gcd_lcm(x, y)
        print(f"GCD = {gcd_val}, LCM = {lcm_val}")

    elif choice == "11":
        n = int(input("Enter a number: "))
        print(f"{n} is Prime" if is_prime(n) else f"{n} is Not Prime")

    elif choice == "12":
        n = int(input("Enter a number: "))
        print(f"{n} is {even_odd(n)}")

    elif choice == "13":
        n = int(input("Enter an integer: "))
        b, o, h = number_conversion(n)
        print(f"Binary: {b}, Octal: {o}, Hexadecimal: {h}")

    elif choice == "14":
        n = int(input("Enter a number: "))
        for line in multiplication_table(n):
            print(line)

    elif choice == "15":
        n = int(input("Enter a number: "))
        print("Sum of digits:", sum_of_digits(n))

    elif choice == "16":
        n = int(input("Enter a number: "))
        print("Reverse:", reverse_number(n))

    elif choice == "17":
        print("\n--- Calculation History ---")
        for h in view_history():
            print(h)

    elif choice == "18":
        print(clear_history())

    elif choice == "19":
        confirm = input("Are you sure you want to exit? (y/n): ").lower()
        if confirm == "y":
            print("Exiting... Goodbye!")
            break
        else:
            continue

    else:
        print("Invalid choice! Please try again.")
