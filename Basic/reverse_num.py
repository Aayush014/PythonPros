num = int(input("Enter a number: "))

rev_num = 0
while num > 0:
    rev_num = rev_num * 10 + num % 10
    num = num // 10

print("The reversed number is:", rev_num)