debugging = 1
hubs = 0
import time
import random
def type_text(te):
	for c in str(te):
		print(c, end = "")
		time.sleep(random.uniform(.01,.1))
	print("")
def hub():
	while True:
		type_text("Welcome to the hub. I am hubby I will direct you to wherever you want.")
		hubs = 0
		type_text("0 to stop")
		type_text("1 for calculator")
		type_text("2 for number game")
		type_text("3 for palindrome detector")
		type_text("4 for pig latin translator")
		type_text("5 for anagram maker")
		type_text("6 for averager")
		type_text("7 for temperature calculator")
		type_text("8 for area calculator")
		hubs = int(input("what do you want: "))
		if hubs == "":
			type_text("oops looks like you are a bit trigerhappy")
		else:
			if hubs ==0:
				type_text("Goodby please come back soon! ##connection terminated by:Hubby##")
			time.sleep(1)
			quit()
		if hubs ==1:
			type_text("Ok sending you to Calcu.")
			time.sleep(1)
			import calculater
		elif hubs ==2:
			type_text("Ok sending you to Guessy.")
			time.sleep(1)
			import number_game
		elif hubs ==3:
			type_text("Ok sending you to Pally.")
			time.sleep(1)
			import paladrome
		elif hubs ==4:
			type_text("Ok sending you to Pig.")
			time.sleep(1)
			import pig
		elif hubs ==5:
			type_text("Ok sending you to Anny.")
			time.sleep(1)
			import anagram
		elif hubs ==6:
			type_text("Ok sending you to AV (she is a bit crazy).")
			import average
		elif hubs ==7:
			type_text("Ok sending you to Kelven.")
			import temp_calculate_hub
		elif hubs ==8:
			type_text("Ok sending you to Arion.")
			import area_calculater
		elif hubs ==9:
			type_text("Sorry this option is not available yet.")
		elif hubs ==10:
			type_text("Sorry this option is not available yet.")
		elif hubs == 7232010:
			import code
		else:
			type_text("Sorry this option is not available yet.")
if debugging == 0:
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