debuging = 1
hubo = 0
import time
import random
lists = []
def hub():
	while True:
		lists = []
		for i in "Welcome to the hub. I am hubby I will direct you to wherever you want.":
			lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.1))
		print("")
		hubo = 0
		lists = []
		for i in "0 to stop":
			lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.1))
		print("")
		lists = []
		for i in "1 for calculator":
			lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.1))
		print("")
		lists = []
		for i in "2 for number game":
			lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.1))
		print("")
		lists = []
		for i in "3 for paladrome deteector":
			lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.1))
		print("")
		lists = []
		for i in "4 for pig latin translator":
			lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.1))
		print("")
		lists = []
		for i in "5 for anagram maker":
			lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.1))
		print("")
		lists = []
		for i in "6 for averager":
			lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.1))
		print("")
		lists = []
		for i in "7 for temperature calculator":
			lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.1))
		print("")
		lists = []
		for i in "8 for area calculator":
			lists.append(i)
		for x in lists:
			print(x, end = "")
			time.sleep(random.uniform(.01,.1))
		print("")
		hubo = int(input("what do you want: "))
		if hubo == "":
			lists = []
			for i in "opps looks like you are a bit trigerhappy":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
		else:
			if hubo ==0:
				lists = []
				for i in "Goodby please come back soon! ##connection terminated by:Hubby##":
					lists.append(i)
				for x in lists:
					print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
			time.sleep(1)
			quit()
		if hubo ==1:
			lists = []
			for i in "Ok sending you to Calcu.":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
			time.sleep(1)
			import calculator
		elif hubo ==2:
			lists = []
			for i in "Ok sending you to Guessy.":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
			time.sleep(1)
			import number_game
		elif hubo ==3:
			lists = []
			for i in "Ok sending you to Pally.":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
			time.sleep(1)
			import paladrome
		elif hubo ==4:
			lists = []
			for i in "Ok sending you to Pig.":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
			time.sleep(1)
			import pig
		elif hubo ==5:
			lists = []
			for i in "Ok sending you to Anny.":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
			time.sleep(1)
			import anagram
		elif hubo ==6:
			lists = []
			for i in "Ok sending you to AV (she is a bit crazy).":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
			import average
		elif hubo ==7:
			lists = []
			for i in "Ok sending you to Kelven.":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
			import temp_calculator_hub
		elif hubo ==8:
			lists = []
			for i in "Ok sending you to Arion.":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
			import area_calculator
		elif hubo ==9:
			lists = []
			for i in "Sorry this option is not available yet.":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
		elif hubo ==10:
			lists = []
			for i in "Sorry this option is not available yet.":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
				print("")
		elif hubo == 7232010:
			import code
		else:
			lists = []
			for i in "Sorry this option is not available yet.":
				lists.append(i)
			for x in lists:
				print(x, end = "")
				time.sleep(random.uniform(.01,.1))
			print("")
if debuging == 0:
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("initiating")
	time.sleep(1.5)
	print("connection successful")
	time.sleep(1)
	hub()
else:
	hub()