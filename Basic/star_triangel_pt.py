n= 5
a = n
b = n

for x in range(1,n+1):
    for y in range(1,n*2):
        if y == a or y == b or x == n:
            print("*",end="")
        else:
            print(end=" ")
    a = a - 1
    b = b + 1
    print()
print("")    