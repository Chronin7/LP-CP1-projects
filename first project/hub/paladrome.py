from config import debugging
from utils import type_text
import time
def pal():
	type_text("Hi I am Pally")
	invertedP = ""
	doagennP = True
	iterationP = 1
	just_started = 0
	runnerP = "placeholder"
	nameP = str(input("Please input a word or sentence and i will tell you if it's a palindrome or not: ")).lower()
	while doagennP == True:
		invertedP = ""
		iterationP = 1
		if just_started == 1:
			nameP = str(input("Ok input the desired word to be tested:"))
		if len(nameP) == 1:
			print(nameP,"is a palindrome")
			invertedP = ""
			runnerP = str(input("Do you want me to detect another palindrome for you? (y/n): "))
			just_started = 1
			if runnerP == "n":
				type_text("Ok sending you back to Hubby")
				time.sleep(1)
				doagennP = False
		else:
			loopP = (len(nameP))
			lopnarP =(len(nameP))
			for lopnarP in range(lopnarP):
					invertedP += nameP[loopP-iterationP]
					iterationP += 1
			if invertedP == nameP:
				print(nameP,"is a palindrome")
			else:
				print(nameP,"is not a palindrome")
				runnerP = str(input("Do you want me to detect another palindrome for you? (y/n): ")).lower()
				just_started = 1
				if runnerP == "n":
					type_text("ok sending you back to Hubby")
					time.sleep(1)
					doagennP = False