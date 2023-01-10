def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def float(x,y):
    return(x/y)
print("select operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choice=input("enter the choice(1\2\3\4:")
num1=int(input("enter the number"))
num2=int(input("enter the number"))
if choice ==1:
        print("num1=="+",num2="==",add[num1,num2]")
elif choice==2:
        print("num1=="-",num2"==",sub[num1,num2]")
elif choice==3:
        print("num1=="*",num2"==",mul[num1,num2]")
elif choice==4:
        print("num1=="/",num2"==",div[num1,num2]")
else:
    print("invalid input")
    
        
