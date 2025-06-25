def calculator():
    print("Simple Calculator")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        try:
            # Get user input
            choice = input("Enter operation (1/2/3/4/5): ")
            
            if choice == '5':
                print("Exiting calculator...")
                break
                
            if choice not in ('1', '2', '3', '4'):
                print("Invalid input. Please try again.")
                continue
                
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                    
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            
        # Ask if user wants another calculation
        another = input("Perform another calculation? (yes/no): ").lower()
        if another != 'yes':
            print("Exiting calculator...")
            break

# Run the calculator
calculator()