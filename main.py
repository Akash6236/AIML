import calculator

num1=float(input("enter the first number"))
num2=float(input("enter the second number"))

print("\n chose an operation:")

print("1.Addition")
print("1.subtraction")
print("1.Multiplication")
print("1.Divison")

choice=int(input("enter your choice (1-4):"))
if choice==1:
    print("result=",calculator.add(num1,num2))

elif choice==2:
    print("result=",calculator.subtract(num1,num2))

elif choice==3:
    print("result=",calculator.multiply(num1,num2))

elif choice==4:
    print("result=",calculator.divide(num1,num2))

else:
    print("invalid choice")

    