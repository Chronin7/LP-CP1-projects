import time
import random
lists = []
def type_line(te):
	for c in str(te):
		print(c, end = "")
		time.sleep(random.uniform(.01,.1))
	print("")
type_line("Hi i am Arion. I am a area finder")
while True:
	type_line("1 for square/rectangle")
	type_line("2 for triangle")
	type_line("3 for circle")
	type_line("4 for trapezoid")
	shape = int(input("what do you want or type stop to stop: "))
	if shape == "1":
		#square/rectangle
		type_line("ok input the numbers that you want")
		a = int(input("what is the hight (only numbers please): "))
		b = int(input("what is the length (only numbers please): "))
		type_line(f"when the hight is {a} and the length is {b} the area is {a*b}.")
		e = 1
	if shape == "3":
		#triangle

		type_line("ok input the numbers that you want")
		e = 1
		a = int(input("what is the hight (only numbers please): "))
		type_line(f"when the radius is {a} the area is {3.141592653589793238462643383279*a^2}")
	if shape == "2":
		#scrcal
		type_line("ok input the numbers that you want")
		e = 1
		a = int(input("what is the hight (only numbers please): "))
		b = int(input("what is the length (only numbers please): "))
		type_line(f"when the hight is {a} and the length is {b} the area is {(a*b)*(1/2)}.")
	if shape == "4":
		#trapisoid
		type_line("ok input the numbers that you want")
		e = 1
		a = int(input("what is the hight (only numbers please): "))
		b = int(input("what is the top (only numbers please): "))
		c = int(input("what is the bottom (only numbers please): "))
		type_line(f"when the hight is {a} and the bottom is {b} and the top is {c} the area is {((b+c)/2)*a}.")
	if shape == "5":
		type_line("sorry coming soon")
		e = 0
	if shape == "6":
		type_line("sorry coming soon")
		e = 0
	if shape == "7":
		type_line("sorry coming soon")
		e = 0
	if shape == "8":
		type_line("sorry coming soon")
		e = 0
	if shape == "9":
		type_line("sorry coming soon")
		e = 0
	if shape == "10":
		type_line("sorry coming soon")
		e = 0
	if shape == "11":
		type_line("sorry coming soon")
		e = 0
	if shape == "12":
		type_line("sorry coming soon")
		e = 0
	if shape == "13":
		type_line("sorry coming soon")
		e = 0
	if shape == "14":
		type_line("sorry coming soon")
		e = 0
	if shape == "15":
		type_line("sorry coming soon")
		e = 0
	if shape == "16":
		type_line("sorry coming soon")
		e = 0
	if shape == "17":
		type_line("sorry coming soon")
		e = 0
	if shape == "18":
		type_line("sorry coming soon")
		e = 0
	if shape == "19":
		type_line("sorry coming soon")
		e = 0
	if shape == "20":
		type_line("sorry coming soon")
		e = 0
	if shape == "stop":
		type_line("ok sending you back to Hubby")
		break
	else:
		type_line("sorry coming soon")
		e = 0
	if e == 1:
		type_line("sorry i didn't understand")
		e = 0