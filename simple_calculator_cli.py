# calculator.py
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Choose operation (+, -, *, /): ")

        if operator == '+':
            print(f"Result: {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1 * num2}")
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print(f"Result: {num1 / num2}")
        else:
            print("Invalid operator selected.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    calculator()
