import random
number=random.randint(1,10)

while(True):
    num=int(input("Enter the number between 1 to 10 :"))

    if(num==number):
       print("correct")
       break
    else:
       print("enter again")      
