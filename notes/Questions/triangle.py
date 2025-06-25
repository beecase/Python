a=int(input("Enter the first side"))
b=int(input("Enter the second side"))
c=int(input("Enter the third side"))
if(a==b==c):
    print("The triangle is equilateral")
elif(a==b or b==c or c==a):
    print("the triangle is isosceles")
else:
    print("the triangle is scalene")

