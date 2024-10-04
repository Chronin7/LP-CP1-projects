import time
import random
def type_line(str):
	for c in str:
		print(c, end = "")
		time.sleep(random.uniform(.01,.1))
	print("")
lists = []
type_line("hi this is Kelven")
def temp():
	while True:
		yes = input("would you like celsius to fahrenheit (y/n): ")
		if yes == "y":
			tempofcelsius = int(input("what is the temp in celsius: "))
		type_line("the temp for fahrenheit when celsius is",tempofcelsius,"is",tempofcelsius*(9/5)+32)
		if yes == "n":
			no = input("would you like celsius to fahrenheit (y/n): ")
			if no == "y":
				tempforfahrenheit = int(input("what is the temp in fahrenheit: "))
				type_line("the temp for celsius when fahrenheit is ",tempforfahrenheit,"is",tempforfahrenheit-32*(5/9))
			else:
				type_line("Ok sending you back to Hubby.")
				break
		else:
			type_line("sorry i didn't understand")
temp()