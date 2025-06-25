num=int(input('Enter a number'))
sum=""
while(num>0):
    rem=num%10
    sum=sum+str(rem)
    num=num//10
rev=int(sum)    
print("Reverse is :",rev)    