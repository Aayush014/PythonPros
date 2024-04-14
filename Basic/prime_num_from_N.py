num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for num in range(num1, num2+1):
    if num < 2:
        continue
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)