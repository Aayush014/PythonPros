def divideNumbers(x, y):
    try:
        result = x / y
        print("Result:", result)
    except ZeroDivisionError:
        print("You can't divide by zero...")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
divideNumbers(a, b)