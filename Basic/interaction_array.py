a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

c = [i for i in a if i in b]
print("The intersection of the two arrays is:", c)