print("CALCULATOR PROGRAM:---")
def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num1/num2)
print("operations appeared:-")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
def calculator(num1,num2):
    choice=int(input("enter your choice between(1,2,3,4):---"))
    if(choice==1):
         add(num1,num2)
    elif(choice==2):
        sub(num1,num2)
    elif(choice==3):
        mul(num1,num2)
    else:
         div(num1,num2)
num1=int(input("enter first number:-"))
num2=int(input("enter second number:-"))
calculator(num1,num2)