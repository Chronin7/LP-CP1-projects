debuging = 0
hubo = 0
import time
def hub():
	while True:
		print("Welcome to the hub. I am hubby I will direct you to wherever you want.")
		hubo = 0
		hubo = int(input("1 for calculator 2 for guessing game 3 for palindrome detector 4 for pig latin translator 5 for anagram maker 6 for average and 0 to quit: "))
		if hubo == "":
			print("opps looks like you are a bit trigerhappy")
		else:
			if hubo ==0:
				print("Goodby please come back soon! ##connection terminated by:Hubby##")
				time.sleep(1)
				quit()
			if hubo ==1:
				print("Ok sending you to Calcu.")
				time.sleep(1)
				import calculater
			elif hubo ==2:
				print("Ok sending you to Guessy.")
				time.sleep(1)
				import number_game
			elif hubo ==3:
				print("Ok sending you to Pally.")
				time.sleep(1)
				import paladrome
			elif hubo ==4:
				print("Ok sending you to Pig.")
				time.sleep(1)
				import pig
			elif hubo ==5:
				print("Ok sending you to Anny.")
				time.sleep(1)
				import anagram
			elif hubo ==6:
				print("Ok sending you to AV (she is a bit crazy).")
				import average
			elif hubo ==7:
				print("Sorry this option is not available yet.")
			elif hubo ==8:
				print("Sorry this option is not available yet.")
			elif hubo ==9:
				print("Sorry this option is not available yet.")
			elif hubo ==10:
				print("Sorry this option is not available yet.")
			elif hubo ==3.141:
				print("Sorry this option is not available yet.")
			else:
				print("Sorry this option is not available yet.")


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