import random
tl = " "
tm = " "
tr = " "
ml = " "
mm = " "
mr = " "
bl = " "
bm = " "
br = " "
ai_next = ""
def check_win_X():
	if tl == "X" and tm == "X" and tr == "X":
		return("computer win")
	if tl == "X" and mm == "X" and br == "X":
		return("computer win")
	if tl == "X" and ml == "X" and bl == "X":
		return("computer win")
	if tl == "X" and tm == "X" and tr == "X":
		return("computer win")
	if tm == "X" and mm == "X" and bm == "X":
		return("computer win")
	if tr == "X" and mr == "X" and br == "X":
		return("computer win")
	if tr == "X" and mm == "X" and bl == "X":
		return("computer win")
	if ml == "X" and mm == "X" and mr == "X":
		return("computer win")
	if tl == "O" and tm == "O" and tr == "O":
		return("player win")
	if tl == "O" and mm == "O" and br == "O":
		return("player win")
	if tl == "O" and ml == "O" and bl == "O":
		return("player win")
	if tl == "O" and tm == "O" and tr == "O":
		return("player win")
	if tm == "O" and mm == "O" and bm == "O":
		return("player win")
	if tr == "O" and mr == "O" and br == "O":
		return("player win")
	if tr == "O" and mm == "O" and bl == "O":
		return("player win")
	if ml == "O" and mm == "O" and mr == "O":
		return("player win")
#todo: check ai O check win O 
def check_AI_X():
	if tl == "X" and tm == "X":
		ai_next = "3"
	elif tl == "X" and tr == "X":
		ai_next = "2"
	elif tl == "X" and mm == "X":
		ai_next = "9"
	elif tl == "X" and br == "X":
		ai_next = "5"
	elif tl == "X" and ml == "X":
		ai_next = "7"
	elif tl == "X" and bl == "X":
		ai_next = "4"
	elif tm == "X" and mm == "X":
		ai_next = "8"
	elif tm == "X" and bm == "X":
		ai_next = "5"
	elif tr == "X" and mm == "X":
		ai_next = "7"
	elif tr == "X" and mr == "X":
		ai_next = "9"
	elif tr == "X" and br == "X":
		ai_next = "6"
	elif tr == "X" and bl == "X":
		ai_next = "5"
	elif ml == "X" and mm == "X":
		ai_next = "6"
	elif ml == "X" and mr == "X":
		ai_next = "5"
	elif ml == "X" and tl == "X":
		ai_next = "7"
	elif mm == "X" and tl == "X":
		ai_next = "7"
	elif mm == "X" and tm == "X":
		ai_next = "8"
	elif mm == "X" and tr == "X":
		ai_next = "7"
	elif mm == "X" and ml == "X":
		ai_next = "6"
	elif mm == "X" and mr == "X":
		ai_next = "4"
	elif mm == "X" and bl == "X":
		ai_next = "3"
	elif mm == "X" and bm == "X":
		ai_next = "2"
	elif mm == "X" and br == "X":
		ai_next = "1"
	elif mm == "X" and mr == "X":
		ai_next = "4"
	elif mm == "X" and br == "X":
		ai_next = "1"
	elif mr == "X" and mm == "X":
		ai_next = "4"
	elif mr == "X" and ml == "X":
		ai_next = "5"
	elif mr == "X" and tr == "X":
		ai_next = "9"
	elif mr == "X" and br == "X":
		ai_next = "3"
	elif bl == "X" and tl == "X":
		ai_next = "4"
	elif bl == "X" and tr == "X":
		ai_next = "5"
	elif bl == "X" and ml == "X":
		ai_next = "1"
	elif bl == "X" and mm == "X":
		ai_next = "3"
	elif bl == "X" and bm == "X":
		ai_next = "9"
	elif bl == "X" and br == "X":
		ai_next = "8"
	elif bm == "X" and tm == "X":
		ai_next = "5"
	elif bm == "X" and mm == "X":
		ai_next = "2"
	elif bm == "X" and bl == "X":
		ai_next = "9"
	elif bm == "X" and br == "X":
		ai_next = "7"
	elif br == "X" and tl == "X":
		ai_next = "5"
	elif br == "X" and tr == "X":
		ai_next = "6"
	elif br == "X" and mm == "X":
		ai_next = "1"
	elif br == "X" and mr == "X":
		ai_next = "3"
	elif br == "X" and bl == "X":
		ai_next = "8"
	elif br == "X" and bm == "X":
		ai_next = "7"
	else:
		return("null")
	return
def print_ui():
	print(f"{tl}  |  {tm}  |  {tr}",flush=False)
	print(f"_____________",flush=False)
	print(f"{ml}  |  {mm}  |  {mr}",flush=False)
	print(f"_____________",flush=False)
	print(f"{bl}  |  {bm}  |  {br}",flush=False)
while True:
	tl = " "
	tm = " "
	tr = " "
	ml = " "
	mm = " "
	mr = " "
	bl = " "
	bm = " "
	br = " "
	print("0 to quit")
	print("1 to play computer")
	print("2 to play player")
	play = int(input("what do you want: "))
	if play == 0:
		quit
	elif play == 1:
		turn = int(input("""1 to go first
2 to go second
what do you want: """))
		if turn == 1:
			print("")
		elif turn == 2:
			while True:
				if check_AI_X() == "null":
					while True:
						rand = random.randint(1,4)
						if rand == 1 and tl == " ":
							tl = "X"
							break
						elif rand == 2 and bl == " ":
							bl = "X"
							break
						elif rand == 3 and br == " ":
							br = "X"
							break
						elif rand == 4 and tr == " ":
							tr = "X"
							break
					print_ui()
					while True:
						print("1 for top left")
						print("2 for top middle")
						print("3 for top right")
						print("4 for middle left")
						print("5 for middle middle")
						print("6 for middle right")
						print("7 for bottom left")
						print("8 for bottom middle")
						print("9 for bottom right")
						play_go = int(input("where do you want to go: "))
						if play_go == 1:
							print("that is alredy taken")
						if play_go == 2:
							print("that is alredy taken")
						if play_go == 3:
							print("that is alredy taken")
						if play_go == 4:
							print("that is alredy taken")
						if play_go == 5:
							print("that is alredy taken")
						if play_go == 6:
							print("that is alredy taken")
						if play_go == 7:
							print("that is alredy taken")
						if play_go == 8:
							print("that is alredy taken")
						if play_go == 9:
							print("that is alredy taken")
						else:
							break
					print_ui()
					if mm == "O":
						non_standerd()
	elif play == 2:
		redplayone = input("who is player 1: ")
		redplaytwo = input("who is player 2: ")
	else:
		print("sorry i didn't understand")