import random
choices=["snake","Water","Gun"]
computer=random.choice(choices)
user=input("Enter snake,water,gun: ").lower()
print("computer choice :",computer)

if(user==computer):
    print("draw")
elif(user=="water" and computer=="gun"):
    print("you win! water damage gun")
elif(user=="snake" and computer=="water"):
    print("you win! snake drink water") 
elif(user=="gun" and computer=="snake"):
    print("you win! gun kills snake")          
elif(user in choices):
    print("you lose!")
else:
    print("Invalid input")        