option=[1,2,3,4,5,6]
print(option)
import random
p='y'
while(p=='y'):
    c=0
    user_num=int(input("choose number"))
    price=int(input("Enter the bet"))


    for i in range(1,7):
        num=random.randint(1,6)
        print(f"rolling{i} times: ")
        print(num)
        if(user_num==num):
            c=c+1
        
    if(c>2):
        print("YOU WIN",c*price)
    else:
         print("YOU LOSE")
    p= input("Do you want to play again y/n")    
  