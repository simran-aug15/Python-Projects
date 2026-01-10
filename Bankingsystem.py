Balance=100000

while(True):
    print("Bank Menu :")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.exit")
    choice=int(input("Enter your choice "))
    if(choice==1):
        amount=int(input("Enter the amount: "))
        Balance+=amount
        print("Amount depoisted successfully")
    elif(choice==2):
        amount=int(input("Enter the amount: "))
        if(amount<=Balance):
          Balance-=amount
          print("Please collect your cash ")
        else:
            print("Not a sufficient balance")  
    elif(choice==3):
        print("The Balance is: ",Balance)
    elif(choice==4):
        print("Thank you")
        break 
    else:
        print("Invalid choice")       
