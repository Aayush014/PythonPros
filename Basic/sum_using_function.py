def sumOfDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumOfDigits(n // 10)

num = int(input("Enter a number: "))
result = sumOfDigits(num)
print("The sum of the digits of", num, "is:", result)