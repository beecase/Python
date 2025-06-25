def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
num=int(input("Enter the number"))
print(f"The factorial of {num} is: {fact(num)}")




    
