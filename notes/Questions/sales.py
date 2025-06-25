amount=int(input("enter the amount"))
if(amount<=5000):
    discount=5/100 *amount
    print(f"congrats, you got Rs {discount} discount")
if(amount>5000 and amount<=10000):
    discount=10/100 *amount
    print(f"congrats, you got Rs {discount} discount")
if(amount>10000):
    discount=15/100 *amount
    print(f"congrats, you got Rs {discount} discount")

