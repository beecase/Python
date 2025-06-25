#WAP to find gcd
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
num1=int(input("enter the number"))    
num2=int(input("enter the number"))      
print(f"The gcd of {num1} and {num2} is: {gcd(num1,num2)}")
    
    