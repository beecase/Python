num=int(input("enter the number"))
c=0
if (num==1):
    print(f"{num} is not prime")
else:    
    for i in range(1,num):
        if(num%i==0):
         c=c+1
    if(c>1):
     print(f"{num} is not prime")
    else:
     print(f"{num} is a prime number")
