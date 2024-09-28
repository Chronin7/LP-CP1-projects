operation = 0
conferm = 0
a = "n/a"
b = "n/a"
print("Hi this is Calcu. What do you want me to calculate today")
def calcu():
    while True:
        print("0 to stop")
        print("1 for devison")
        print("2 for multipulcation")
        print("3 for subtaction")
        print("4 for addition")
        print("5 for modulo")
        print("6 for factoring")
        operation = input("what do you want: ").lower()
        if operation == "":
            print("opps looks like you are a bit trigerhappy")
        else:
            if operation == "0":
                print("ok sending you back to Hubby.")
                break
            if operation == "1" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                    print("oops looks like you are a bit trigerhappy")
                            else:
                                if b == 0 :
                                    print("division by 0 error")
                                else:
                                    print(a,"/",b,"=",a/b)
                                    break
            if operation == "2" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                print("oops looks like you are a bit trigerhappy")
                            else:
                                print(a,"X",b,"=",a*b)
            if operation == "3" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                print("oops looks like you are a bit trigerhappy")
                            else:
                                print(a,"-",b,"=",a-b)
            if operation == "4" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                print("oops looks like you are a bit trigerhappy")
                            else:
                                print(a,"+",b,"=",a+b)
            if operation == "5" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                print("oops looks like you are a bit trigerhappy")
                            else:
                                print(a,"%",b,"=",a%b)
            if operation == "6" :
                while True:
                    a = int(input("what is the first number:"))
                    if a == "":
                        print("oops looks like you are a bit trigerhappy")
                    else:
                        while True:
                            b = int(input("what is the second number:"))
                            if b == "":
                                print("oops looks like you are a bit trigerhappy")
                            else:
                                print(a,"^",b,"=",a**b)
calcu()