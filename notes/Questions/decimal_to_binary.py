# decimal = 13 
# binary = ""

# #while decimal > 0:
#     remainder = decimal % 2
#     binary = str(remainder) + binary
#     decimal = decimal // 2

# print("Binary:", binary)
decimal = int(input("Enter the number"))
binary_digits = []

while decimal > 0:
    remainder = decimal % 2
    binary_digits.append(str(remainder))  # store as string for easy joining
    decimal = decimal // 2

# reverse the list to get the correct binary order
binary_digits.reverse()

# # join the list into a string
binary = ''.join(binary_digits)


print("Binary:", binary)
