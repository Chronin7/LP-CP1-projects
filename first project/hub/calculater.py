operation = 0
conferm = 0
a = "n/a"
b = "n/a"
print("Hi this is Calcu. What do you want me to calculate today")
def calcu():
    while True:
        operation = input("Do you want to do division, multiplication, subtraction, addition, modulo, factoring or type stop to stop (I am picky so type the operation the same as shown here.): ").lower()
        if operation == "":
            print("opps looks like you are a bit trigerhappy")
        else:
            if operation == "stop":
                print("ok sending you back to Hubby.")
                break
            if operation == "division" :
                a = int(input("what is the first number:"))
                b = int(input("what is the second number:"))
                if b == 0 :
                    print("division by 0 error")
                else:
                    print(a,"/",b,"=",a/b)
            if operation == "multiplication" :
                a = int(input("what is the first number:"))
                b = int(input("what is the second number:"))
                print(a,"X",b,"=",a*b)
            if operation == "subtraction" :
                a = int(input("what is the first number:"))
                b = int(input("what is the second number:"))
                print(a,"-",b,"=",a-b)
            if operation == "addition" :
                a = int(input("what is the first number:"))
                b = int(input("what is the second number:"))
                print(a,"+",b,"=",a+b)
            if operation == "modulo" :
                a = int(input("what is the first number:"))
                b = int(input("what is the second number:"))
                print(a,"%",b,"=",a%b)
            if operation == "factoring" :
                a = int(input("what is the first number:"))
                b = int(input("what is the second number:"))
                print(a,"^",b,"=",a**b)
            if operation == "stop" :
                print("sending you to Hubby.")
                break

calcu()