n = int(input("Enter the Number: "))
isPrime = False

if (n <= 1):
    isPrime = False
elif (n <= 3):
    isPrime = True
elif (n % 2 == 0 or n % 3 == 0):
    isPrime = False
else:
    for i in range(5, int(n**0.5) + 1, 6):  
        if n % i == 0 or n % (i + 2) == 0:
            is_prime = False
            break
    else:
        isPrime = True

if isPrime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")