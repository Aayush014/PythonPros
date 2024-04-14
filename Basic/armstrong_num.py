num = int(input("Enter a number: "))
n_str = str(num)

sum = 0
for digit in n_str:
    sum += int(digit)**len(n_str)

if sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")