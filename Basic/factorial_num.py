num = int(input("Enter any Number: "))
fact = 1

if(num<0):
    print("Factorial dosen't exist")
elif(num == 0):
    print("Factorial is 1")    
else:
    for i in range(1, num+1):
        fact = fact*i
    print("The Facorial of ",num, "is", fact,)