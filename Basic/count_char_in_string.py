str1 = "Hello, World!"
exclude_char = " "

char = "l"

count = str1.count(char) - str1.count(exclude_char + char)

# Print the count
print("The number of the character", char, "in the string is:", count)