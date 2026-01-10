print("simple calculator")

a=int(input("Enter the Number 1:"))
b=int(input("Enter the number 2:"))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice :"))
if(choice==1):
    print("Result :",a+b)
elif(choice==2):
    print("Result :",a-b)
elif(choice==3):
    print("Result :",a*b)
elif(choice==4):
    print("Result :",a/b) 
else:
    print("invalid input")               

