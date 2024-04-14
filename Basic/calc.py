num1 = int(input("Enter first Value:-"))
num2 = int(input("Enter second Value:-"))

operator = input("Enter the operator (+, -, *, /, exit): ")

while operator!= 'exit':
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 / num2
        case _:
            print("Invalid operator")
            result = None

    # Print the result
    if result is not None:
        print("The result is:", result)

    # Get the operator from the user
    operator = input("Enter the operator (+, -, *, /, exit): ")