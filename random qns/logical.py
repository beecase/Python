a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Using 'and' operator
if a > 5 and b > 15:
    print("Both conditions are True (a > 5 and b > 15)")
else:
    print(" One or both conditions are False (a > 5 and b > 15)")

# Using 'or' operator
if a > 15 or b > 15:
    print(" At least one condition is True (a > 15 or b > 15)")
else:
    print("Both conditions are False (a > 15 or b > 15)")

# Using 'not' operator
if not (a > 15):
    print("a is NOT greater than 15 (not (a > 15))")
else:
    print("a is greater than 15")
if not (b > 15):
    print("b is NOT greater than 15 (not (a > 15))")
else:
    print("b is greater than 15")