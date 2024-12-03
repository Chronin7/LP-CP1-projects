import time
from utils import type_text
from config import debugging
from calculater import calcu
from area_calculater import area
from anagram import anagram
from average import run
from code import tuchy
from number_game import game
from paladrome import pal
from pig import call
from temp_calculate_hub import farinhight451
from settings import changeSettings
hubo = 0
def hub():
	while True:
		type_text("Welcome to the hub. I am hubby I will direct you to wherever you want.")
		hubo = 0
		type_text("0 to stop")
		type_text("1 for settings")
		type_text("2 for calculator")
		type_text("3 for number game")
		type_text("4 for palindrome detector")
		type_text("5 for pig latin translator")
		type_text("6 for anagram maker")
		type_text("7 for averager")
		type_text("8 for temperature calculator")
		type_text("9 for area calculator")
		hubo = int(input("what do you want: "))
		if hubo == "":
			type_text("oops looks like you are a bit trigerhappy")
		else:
			if hubo ==0:
				type_text("Goodby please come back soon! ##connection terminated by:Hubby##")
			time.sleep(1)
			quit()
		if hubo ==2:
			type_text("Ok sending you to Calcu.")
			time.sleep(1)
			calcu(1)
		elif hubo ==3:
			type_text("Ok sending you to Guessy.")
			time.sleep(1)
			game(1)
		elif hubo ==4:
			type_text("Ok sending you to Pally.")
			time.sleep(1)
			pal(1)
		elif hubo ==5:
			type_text("Ok sending you to Pig.")
			time.sleep(1)
			call(1)
		elif hubo ==6:
			type_text("Ok sending you to Anny.")
			time.sleep(1)
			anagram(1)
		elif hubo ==7:
			type_text("Ok sending you to AV (she is a bit crazy).")
			run(1)
		elif hubo ==8:
			type_text("Ok sending you to Kelvin.")
			farinhight451(1)
		elif hubo ==9:
			type_text("Ok sending you to Arion.")
			area()
		elif hubo ==11:
			type_text("Sorry this option is not available yet.")
		elif hubo ==10:
			type_text("Sorry this option is not available yet.")
		elif hubo ==1:
			changeSettings()
		elif hubo == 7232010:
			tuchy()
		else:
			type_text("Sorry this option is not available yet.")

if not debugging:
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