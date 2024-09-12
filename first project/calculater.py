operation = 0
conferm = 0
a = "n/a"
b = "n/a"
print("Hi this is Calcu. What do you want me to calculate today")
def calcu():
    operation = input("Do you want to do division, multiplication, subtraction, addition, modulo, or factoring: ")
    if operation == "division" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        if b == 0 :
            print("division by 0 error")
            calcu()
        else:
            print(a,"/",b,"=",a/b)
            calcu()
    if operation == "multiplication" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        print(a,"X",b,"=",a*b)
        calcu()
    if operation == "subtraction" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        print(a,"-",b,"=",a-b)
        calcu()
    if operation == "addition" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        print(a,"+",b,"=",a+b)
        calcu()
    if operation == "modulo" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        print(a,"%",b,"=",a%b)
        calcu()
    if operation == "factoring" :
        a = int(input("what is the first number:"))
        b = int(input("what is the second number:"))
        print(a,"^",b,"=",a**b)
        calcu()
    if operation == "stop" :
        quit
    print("Sorry I didn't understand")
    calcu()




operation = input("Do you want to do division, multiplication, subtraction, addition, modulo, or factoring:  ")
if operation == "division" :
    a = int(input("what is the first number:"))
    b = int(input("what is the second number:"))
else:
    if b == 0 :
        print("division by 0 error")
        calcu()
        print(a,"/",b,"=",a/b)
        calcu()
if operation == "multiplication" :
    a = int(input("what is the first number:"))
    b = int(input("what is the second number:"))
    print(a,"X",b,"=",a*b)
    calcu()
if operation == "subtraction" :
    a = int(input("what is the first number:"))
    b = int(input("what is the second number:"))
    print(a,"-",b,"=",a-b)
    calcu()
if operation == "addition" :
    a = int(input("what is the first number:"))
    b = int(input("what is the second number:"))
    print(a,"+",b,"=",a+b)
    calcu()
if operation == "modulo" :
    a = int(input("what is the first number:"))
    b = int(input("what is the second number:"))
    print(a,"%",b,"=",a%b)
    calcu()
if operation == "factoring" :
    a = int(input("what is the first number:"))
    b = int(input("what is the second number:"))
    print(a,"^",b,"=",a**b)
    calcu()
print("Sorry I didn't understand")

calcu()