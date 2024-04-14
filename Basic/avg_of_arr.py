def calculate_average(arr):
    total = sum(arr)
    avg = total / len(arr)
    return avg

arr = [25, 30, 35, 40, 13]
avg = calculate_average(arr)
print("The average is:", avg)