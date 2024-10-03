import time
import random
lists = []
for i in "hi this is kelven":
	lists.append(i)
for x in lists:
	print(x, end = "")
	time.sleep(random.uniform(.01,.2))
print("")
def temp():
	while True:
		yes = input("woud you like celsius to fahrenheit (y/n): ")
		if yes == "y":
			tempofcelsius = int(input("what is the temp in celsius: "))
		lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.2))
		print("")
		print ("the temp for fahrenheit when celsius is",tempofcelsius,"is",tempofcelsius*(9/5)+32)
		if yes == "n":
			no = input("woud you like celsius to fahrenheit (y/n): ")
			if no == "y":
				tempforfahrenheit = int(input("what is the temp in fahrenheit: "))
				print("the temp for celsius when fahrenheight is ",tempforfahrenheit,"is",tempforfahrenheit-32*(5/9))
			else:
				for i in "Ok sending you back to Hubby.":
					lists.append(i)
				for x in lists:
					print(x, end = "")
					time.sleep(random.uniform(.01,.2))
				print("")
				break
		else:
			lists = []
			for i in "sorry i dident understand":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.2))
			print("")
temp()