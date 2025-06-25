#Wap to print fibonacci
def fibo(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("enter the no. of terms"))
for i in range(n):
    print(fibo(i))    