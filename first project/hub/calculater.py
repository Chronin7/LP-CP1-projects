from config import debugging
from utils import type_text
def calcu(operation):
	operation = 0
	type_text("Hi this is Calcu. What do you want me to calculate today")
	a = "n/a"
	b = "n/a"
	while True:
		type_text("0 to stop")
		type_text("1 for division")
		type_text("2 for multiplication")
		type_text("3 for subtraction")
		type_text("4 for addition")
		type_text("5 for modulo")
		type_text("6 for factoring")
		operation = input("what do you want: ").lower()
		if operation == "":
			type_text("oops looks like you are a bit trigerhappy")
		else:
			if operation == "0":
				type_text("ok sending you back to Hubby.")
				break
			if operation == "1" :
				while True:
					a = int(input("what is the first number:"))
					if a == "":
						type_text("oops looks like you are a bit trigerhappy")
					else:
						while True:
							b = int(input("what is the second number: "))
							if b == "":
									type_text("oops looks like you are a bit trigerhappy")
							else:
								if b == 0 :
									type_text("division by 0 error")
								else:
									print(a,"/",b,"=",a/b)
									break
			if operation == "2" :
				while True:
					a = int(input("what is the first number: "))
					if a == "":
						type_text("oops looks like you are a bit trigerhappy")
					else:
						while True:
							b = int(input("what is the second number: "))
							if b == "":
								type_text("oops looks like you are a bit trigerhappy")
							else:
								print(a,"X",b,"=",a*b)
			if operation == "3" :
				while True:
					a = int(input("what is the first number: "))
					if a == "":
						type_text("oops looks like you are a bit trigerhappy")
					else:
						while True:
							b = int(input("what is the second number:"))
							if b == "":
								type_text("oops looks like you are a bit trigerhappy")
							else:
								print(a,"-",b,"=",a-b)
			if operation == "4" :
				while True:
					a = int(input("what is the first number:"))
					if a == "":
						type_text("oops looks like you are a bit trigerhappy")
					else:
						while True:
							b = int(input("what is the second number:"))
							if b == "":
								type_text("oops looks like you are a bit trigerhappy")
							else:
								print(a,"+",b,"=",a+b)
			if operation == "5" :
				while True:
					a = int(input("what is the first number:"))
					if a == "":
						type_text("oops looks like you are a bit trigerhappy")
					else:
						while True:
							b = int(input("what is the second number:"))
							if b == "":
								type_text("oops looks like you are a bit trigerhappy")
							else:
								print(a,"%",b,"=",a%b)
			if operation == "6" :
				while True:
					a = int(input("what is the first number:"))
					if a == "":
						type_text("oops looks like you are a bit trigerhappy")
					else:
						while True:
							b = int(input("what is the second number:"))
							if b == "":
								type_text("oops looks like you are a bit trigerhappy")
							else:
								print(a,"^",b,"=",a**b)