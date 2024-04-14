len = int(input("Enter the Length: "))

fib = 1

if (len < 0):
    print("n must be a non-negative integer")
elif len == 0 or len == 1:
    print(len)
else:
     fib(len - 1) + fib(len - 2)
