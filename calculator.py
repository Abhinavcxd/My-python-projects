def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"Result: {num1 + num2}")
                elif choice == '2':
                    print(f"Result: {num1 - num2}")
                elif choice == '3':
                    print(f"Result: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"Result: {num1 / num2}")
                    else:
                        print("Error: Cannot divide by zero.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

calculator()
