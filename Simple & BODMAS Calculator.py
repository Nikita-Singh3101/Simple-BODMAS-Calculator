def normal_calculator():
    print("\n--- Normal Calculator ---")
    print("Select Operation: +  -  *  /  %  //  ** ")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero!")
    elif op == '%':
        print("Result:", num1 % num2)
    elif op == '//':
        print("Result:", num1 // num2)
    elif op == '':
        print("Result:", num1 ** num2)
    else:
        print("Invalid operator!")


def bodmas_calculator():
    print("\n--- BODMAS Expression Calculator ---")
    print("Enter a valid expression (like 2+3*(4-1)/2): ")
    expr = input("Expression: ")
    try:
        result = eval(expr)
        print("Result:", result)
    except Exception as e:
        print("Error in expression:", e)


def main():
    while True:
        print("\n===== Dual Calculator =====")
        print("1. Normal Calculator")
        print("2. BODMAS Calculator")
        print("3. Exit")
        choice = input("Choose option (1/2/3): ")

        if choice == '1':
            normal_calculator()
        elif choice == '2':
            bodmas_calculator()
        elif choice == '3':
            print("Exiting Calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


# Start the calculator application
main()
