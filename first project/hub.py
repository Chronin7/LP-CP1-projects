import random
import time
debuging = 0
invertedP = ""
iterationP = 1
runnerP = ""
var = 0
hubo = 0
operation = 0
easterEggCount = 2
maxGuessCount = 20
minGuess = 1
maxGuess = 100
playCount = 0
playAgain = True
infinite = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17}
def farinhight451():
	print("hi this is Kelvin")
	while True:
		yes = input("would you like celsius to fahrenheit (y/n): ")
		if yes == "y":
			tempofcelsius = int(input("what is the temp in celsius: "))
			print ("the temp for fahrenheit when celsius is",tempofcelsius,"is",tempofcelsius*(9/5)+32)
		if yes == "n":
			no = input("would you like celsius to fahrenheit (y/n): ")
			if no == "y":
				tempforfahrenheit = int(input("what is the temp in fahrenheit: "))  
				print("the temp for celsius when fahrenheit is ",tempforfahrenheit,"is",tempforfahrenheit-32*(5/9))
			elif no == "n":				
				print("Ok sending you back to Hubby.")
				break
			else:
				print("sorry i didn't understand")
def translate_word(input_word):
	split = {}
	deleted = ""
	not_a_string = ""
	output = ""
	decoded = ""
	j = 0
	i = 0
	x = 0
	iteration = 1
	consonants = []
	if len(input_word) < 3:
		return(input_word)
	else:
		for x in input_word:
			if x == "a":
				deleted = "a"
				split = second_half(iteration, input_word)
				break
			if x == "e":
				deleted = "e"
				split = second_half(iteration, input_word)
				break
			if x == "i":
				deleted = "i"
				split = second_half(iteration, input_word)
				break
			if x == "o":
				deleted = "o"
				split = second_half(iteration, input_word)
				break
			if x == "u":
				deleted = "u"
				split = second_half(iteration, input_word)
				break
			if x == "y" and iteration > 1:
				deleted = "y"
				split = second_half(iteration, input_word)
				break
			iteration += 1
			consonants.append(x)
	for i in split:
		not_a_string = not_a_string + i
	for j in consonants:
		decoded = decoded + j
	output =deleted + not_a_string + decoded + "ay"
	return(output)
def second_half(num,word):
	return (word[num:])
def last_bit():
	while True:
		iteration = 1
		out = ""
		imput_o_word = input("what do you want to translate or type stop to go back to Hubby: ")
		if imput_o_word == "stop":
			type_text("Ok sending you back to hubby. Oink")
			break
		output = []
		intt = imput_o_word.split(" ")
		for i in intt:
			output.append(translate_word(i))
		for x in output:
			if iteration ==1:
				out = out + x
			else:
				out = out +" "+ x
			iteration += 1
		print(out)
def callit():
	print("Hi i am Pig")
	last_bit()
def lists():
	clist = input("what is the name of your list: ")
	thelist = []
	while True:
		action = input("""what do you want to do
	1 add item
	2 remove item
	3 to print and leave the list (note this also deletes it): """)
		if action != "1" and action != "2" and action != "3":
			print("i am not impressed with your efforts to brake me")
		if action == "1" or action == "2" or action == "3":	
			if action == "1":
				inpuy = input("what do you want to add: ")
				thelist.append(inpuy)
			elif action == "2":
				print()
				print(f"          {clist}          ")
				print("___________________________")
				iteration = 1
				for x in thelist:
					print(f"| ⦿ {iteration}: {x}")
				print("___________________________")
				while True:
					remove = int(input("what do you want to remove(0 to stop): "))
					if remove > len(thelist):
						print(f"you dont have a item at {remove}")
					elif remove < 0:
						print("i am not impressed with your efforts to brake me")
					else:
						if remove == 0:
							break
						else:
							del thelist[remove-1]
							break
			elif action == "3":
				print()
				print(f"          {clist}          ")
				print("___________________________")
				iteration = 1
				for x in thelist:
					print(f"| ⦿ {iteration}: {x}")
					iteration += 1
				print("___________________________")
				clist = input("what is the new name for the new list: ")
				thelist = []			
def tuchy():
	input_o_code = input("shhhh. this is a secret i am liam what is the code(only numbers please): ")
	break_it = 1
	binary = ""
	check = 0
	for i in input_o_code:
		binary = binary + str(bin(ord(i)))
	if binary == "0b11011100b11001010b11101100b11001010b11100100b1000000b11001110b11101010b11011100b11011100b11000010b1000000b11001110b11010010b11101100b11001010b1000000b11110010b11011110b11101010b1000000b11101010b11100000b100001":
		while True:
			code_decode = int(input("would you like to code (1) or decode (2) or stop (3): "))
			list_o_coded = []
			output =""
			decoded = ""
			iteration = 1
			loops_o_codeing = 0
			list_o_decoding = []
			if code_decode == 1:
				code = input("what is the uncoded word: ")
				seed = int(input("what is the decoding seed (whole numbers please): "))
				for x in code:
					list_o_coded.append(((ord(x))))
				for y in list_o_coded:
					if loops_o_codeing == 0:
						output = str(int(y)+seed)
					else:
						output = output +","+ str(int(y)+seed)
					loops_o_codeing += 1
				print(output)
			if code_decode == 2:
				coded_decoder = str(input("what is the coded thing: "))
				seed_o_decodeing = int(input("what is the seed: "))
				list_o_decoding = (coded_decoder.split(","))
				for z in list_o_decoding:
					var = str(chr(int(z)-seed_o_decodeing))
					decoded = decoded + var
				print(decoded)
			if code_decode == 3:
				input_o_code = ""
				break_it = 0
				break
	if break_it == 1:
		print('"File "/workspaces/codespaces-jupyter/test.py," line 9"')
		print(f"pickle.({input_o_code})")
		print("		^")
		print("SyntaxError: invalid syntax")
		quit()
	else:
		print("ok sending you back to hubby")
def run():
	print("I am AV the Avenger.")
	while True:
		runs = 1
		list_o_nums = []
		percentage = 0
		classes = input("How many things do you want to average or type stop to stop: ")
		if classes == "stop":
			print("ok sending you back to Hubby")
			break
		classes = int(classes)
		for x in range(classes):
			one_at_a_time = int(input(f"what is the percentage of # {runs} (only numbers please): "))
			percentage += one_at_a_time
			list_o_nums.append(one_at_a_time)
			runs += 1
		print(f"you entered {list_o_nums} #'s it is an average of {percentage/classes}")
		go_agin = input("do you want to use again (y/n): ")
		if go_agin == "n":
			print("ok sending you back to Hubby")
			break
def area():
	print("Hi i am Arion. I am a area finder")
	while True:
		e = 1
		print("1 for rectangle")
		print("2 for square")
		print("3 for triangle")
		print("4 for circle")
		print("5 for trapezoid")
		shape = int(input("what do you want or type stop to stop: "))
		if shape == "1":
			#square/rectangle
			print("ok input the numbers that you want")
			a = int(input("what is the hight (only numbers please): "))
			b = int(input("what is the length (only numbers please): "))
			print(f"when the hight is {a} and the length is {b} the area is {a*b}.")
			e = 0
		if shape == "4":
			#circle
			print("ok input the numbers that you want")
			e = 0
			a = int(input("what is the hight (only numbers please): "))
			print(f"when the radius is {a} the area is {3.141592653589793238462643383279*a^2}")
		if shape == "3":
			#triangle
			print("ok input the numbers that you want")
			e = 0
			a = int(input("what is the hight (only numbers please): "))
			b = int(input("what is the length (only numbers please): "))
			print(f"when the hight is {a} and the length is {b} the area is {(a*b)*(1/2)}.")
		if shape == "5":
			#trapezoid
			print("ok input the numbers that you want")
			e = 0
			a = int(input("what is the hight (only numbers please): "))
			b = int(input("what is the top (only numbers please): "))
			c = int(input("what is the bottom (only numbers please): "))
			print(f"when the hight is {a} and the bottom is {b} and the top is {c} the area is {((b+c)/2)*a}.")
		if shape == "2":
			print("ok input the numbers that you want")
			e = 0
			a = int(input("what is the length of one of the sides (only numbers please): "))
			print(f"when the hight is {a} and the length is {b} the area is {a*2}.")
			e = 0
		if shape == "6":
			print("sorry coming soon")
			e = 0
		if shape == "7":
			print("sorry coming soon")
			e = 0
		if shape == "8":
			print("sorry coming soon")
			e = 0
		if shape == "9":
			print("sorry coming soon")
			e = 0
		if shape == "10":
			print("sorry coming soon")
			e = 0
		if shape == "11":
			print("sorry coming soon")
			e = 0
		if shape == "12":
			print("sorry coming soon")
			e = 0
		if shape == "13":
			print("sorry coming soon")
			e = 0
		if shape == "14":
			print("sorry coming soon")
			e = 0
		if shape == "15":
			print("sorry coming soon")
			e = 0
		if shape == "16":
			print("sorry coming soon")
			e = 0
		if shape == "17":
			print("sorry coming soon")
			e = 0
		if shape == "18":
			print("sorry coming soon")
			e = 0
		if shape == "19":
			print("sorry coming soon")
			e = 0
		if shape == "20":
			print("sorry coming soon")
			e = 0
		if shape == "stop":
			print("ok sending you back to Hubby")
			break
		else:
			print("sorry coming soon")
			e = 0
		if e == 1:
			print("sorry i didn't understand")
			e = 1
def anagram():
	print("Hi i am Anny")
	while True:
		anagram = []
		output = ""
		doit = "12345"
		word = input("what is the word that you want into anagram or type stop to stop: ")
		if word == "stop":
			print("sending you back to Hubby")
			break
		if word == "":
			print("oops looks like you are a bit trigerhappy")
		else:
			rand = len(word)
			for y in doit:
				output = ""
				anagram = []
				for x in word:
					anagram.insert(random.randint(1,rand),x)
				for i in anagram:
					output = output + i
				print(output)
def pal():
	print("Hi I am Pally")
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
				print("Ok sending you back to Hubby")
				time.sleep(1)
				return
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
					print("ok sending you back to Hubby")
					time.sleep(1)
					return
def hub():
	while True:
		print("Welcome to the hub. I am hubby I will direct you to wherever you want.")
		hubo = 0
		print("0 to stop")
		print("1 for list maker")
		print("2 for calculator")
		print("3 for number game")
		print("4 for palindrome detector")
		print("5 for pig latin translator")
		print("6 for anagram maker")
		print("7 for averager")
		print("8 for temperature calculator")
		print("9 for area calculator")
		hubo = int(input("what do you want: "))
		if hubo == "":
			print("oops looks like you are a bit trigerhappy")
		else:
			if hubo ==0:
				print("Goodby please come back soon! ##connection terminated by:Hubby##")
			time.sleep(1)
			quit()
		if hubo ==2:
			print("Ok sending you to Calcu.")
			time.sleep(1)
			calcu()
		elif hubo ==3:
			print("Ok sending you to Guessy.")
			time.sleep(1)
			game()
		elif hubo ==4:
			print("Ok sending you to Pally.")
			time.sleep(1)
			pal()
		elif hubo ==5:
			print("Ok sending you to Pig.")
			time.sleep(1)
			callit()
		elif hubo ==6:
			print("Ok sending you to Anny.")
			time.sleep(1)
			anagram()
		elif hubo ==7:
			print("Ok sending you to AV (she is a bit crazy).")
			run()
		elif hubo ==8:
			print("Ok sending you to Kelvin.")
			farinhight451()
		elif hubo ==9:
			print("Ok sending you to Arion.")
			area()
		elif hubo ==11:
			print("Sorry this option is not available yet.")
		elif hubo ==10:
			print("Sorry this option is not available yet.")
		elif hubo ==1:
			lists()
		elif hubo == 7232010:
			tuchy()
		else:
			print("Sorry this option is not available yet.")
def calculater():
	operation = 0
	print("Hi this is Calcu. What do you want me to calculate today")
	a = "n/a"
	b = "n/a"
	while True:
		print("0 to stop")
		print("1 for division")
		print("2 for multiplication")
		print("3 for subtraction")
		print("4 for addition")
		print("5 for modulo")
		print("6 for factoring")
		operation = input("what do you want: ").lower()
		if operation == "":
			print("oops looks like you are a bit trigerhappy")
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
							b = int(input("what is the second number: "))
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
					a = int(input("what is the first number: "))
					if a == "":
						print("oops looks like you are a bit trigerhappy")
					else:
						while True:
							b = int(input("what is the second number: "))
							if b == "":
								print("oops looks like you are a bit trigerhappy")
							else:
								print(a,"X",b,"=",a*b)
			if operation == "3" :
				while True:
					a = int(input("what is the first number: "))
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
def game():
	#just to have a bit of fun
	easterEggCount = 100
	#this is the max guess count
	maxGuessCount = 20
	# this is the min and max guess
	minGuess = 1
	maxGuess = 100
	playCount = 0
	playAgain = True
	while playAgain:
		playCount += 1
		if playCount == easterEggCount:
			print("WHY DID YOU WASTE YOUR TIME ON THIS DUMB GAME! DO SOMETHING BETTER WITH YOUR TIME! ##connection terminated by: Guessy## ")
			quit
		num = random.randint (minGuess,maxGuess)
		print(f'Welcome to GUESS THE NUMBER! i am your host Guessy you have {maxGuessCount} attempts before you lose the game. good luck.')
		while True:
			guess = int(input(f'Guess a number {minGuess}-{maxGuess}: '))  
			if guess == "":
				print("oops looks like you are a bit trigerhappy")
			else:
				break
		for x in range(maxGuessCount): 
			while True:
					if guess < num :
						guess = int(input ("the number is larger: "))
						if guess == "":
							print("oops looks like you are a bit trigerhappy")
					elif guess > num :
						guess = int(input ("the number is smaller: "))
						break
					elif guess == "":
						print("oops looks like you are a bit trigerhappy")
					else:
						if guess == num : 
							print("you got it")
							break
						playAgain = input("do you want to play again? (y/n): ")
						if playAgain != "y":
							playAgain = False
							print("ok sending you back to Hubby")
def palindrome():
	invertedP = ""
	doagennP = True
	iterationP = 1
	runnerP = "placeholder"
	while doagennP == True:
		invertedP = ""
		iterationP = 1
		nameP = str(input("hi i am pally please input a word or sentence and i will tell you if it's a palindrome or not: ")).lower()
		if len(nameP) == 1:
				print(nameP,"is a palindrome")
				invertedP = ""
				runnerP = str(input("do you want me to detect another palindrome for you? (y/n): "))
				if runnerP == "n":
						print("ok sending you back to the hub")
						time.sleep(1)
						doagennP = False

						return

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
				runnerP = str(input("do you want me to detect another palindrome for you? (y/n): ")).lower()
				if runnerP == "n":
						print("ok sending you back to hubby")
						time.sleep(1)
						doagennP = False

						return
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