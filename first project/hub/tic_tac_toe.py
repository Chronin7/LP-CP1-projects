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
def check_player_O():
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
def check_player_X():
	if tl == "O" and tm == "O":
		ai_next = "3"
	elif tl == "O" and tr == "O":
		ai_next = "2"
	elif tl == "O" and mm == "O":
		ai_next = "9"
	elif tl == "O" and br == "O":
		ai_next = "5"
	elif tl == "O" and ml == "O":
		ai_next = "7"
	elif tl == "O" and bl == "O":
		ai_next = "4"
	elif tm == "O" and mm == "O":
		ai_next = "8"
	elif tm == "O" and bm == "O":
		ai_next = "5"
	elif tr == "O" and mm == "O":
		ai_next = "7"
	elif tr == "O" and mr == "O":
		ai_next = "9"
	elif tr == "O" and br == "O":
		ai_next = "6"
	elif tr == "O" and bl == "O":
		ai_next = "5"
	elif ml == "O" and mm == "O":
		ai_next = "6"
	elif ml == "O" and mr == "O":
		ai_next = "5"
	elif ml == "O" and tl == "O":
		ai_next = "7"
	elif mm == "O" and tl == "O":
		ai_next = "7"
	elif mm == "O" and tm == "O":
		ai_next = "8"
	elif mm == "O" and tr == "O":
		ai_next = "7"
	elif mm == "O" and ml == "O":
		ai_next = "6"
	elif mm == "O" and mr == "O":
		ai_next = "4"
	elif mm == "O" and bl == "O":
		ai_next = "3"
	elif mm == "O" and bm == "O":
		ai_next = "2"
	elif mm == "O" and br == "O":
		ai_next = "1"
	elif mm == "O" and mr == "O":
		ai_next = "4"
	elif mm == "O" and br == "O":
		ai_next = "1"
	elif mr == "O" and mm == "O":
		ai_next = "4"
	elif mr == "O" and ml == "O":
		ai_next = "5"
	elif mr == "O" and tr == "O":
		ai_next = "9"
	elif mr == "O" and br == "O":
		ai_next = "3"
	elif bl == "O" and tl == "O":
		ai_next = "4"
	elif bl == "O" and tr == "O":
		ai_next = "5"
	elif bl == "O" and ml == "O":
		ai_next = "1"
	elif bl == "O" and mm == "O":
		ai_next = "3"
	elif bl == "O" and bm == "O":
		ai_next = "9"
	elif bl == "O" and br == "O":
		ai_next = "8"
	elif bm == "O" and tm == "O":
		ai_next = "5"
	elif bm == "O" and mm == "O":
		ai_next = "2"
	elif bm == "O" and bl == "O":
		ai_next = "9"
	elif bm == "O" and br == "O":
		ai_next = "7"
	elif br == "O" and tl == "O":
		ai_next = "5"
	elif br == "O" and tr == "O":
		ai_next = "6"
	elif br == "O" and mm == "O":
		ai_next = "1"
	elif br == "O" and mr == "O":
		ai_next = "3"
	elif br == "O" and bl == "O":
		ai_next = "8"
	elif br == "O" and bm == "O":
		ai_next = "7"
	else:
		return("null")
	return
def check_AI_O():
	if tl == "O" and tm == "O":
		ai_next = "3"
	elif tl == "O" and tr == "O":
		ai_next = "2"
	elif tl == "O" and mm == "O":
		ai_next = "9"
	elif tl == "O" and br == "O":
		ai_next = "5"
	elif tl == "O" and ml == "O":
		ai_next = "7"
	elif tl == "O" and bl == "O":
		ai_next = "4"
	elif tm == "O" and mm == "O":
		ai_next = "8"
	elif tm == "O" and bm == "O":
		ai_next = "5"
	elif tr == "O" and mm == "O":
		ai_next = "7"
	elif tr == "O" and mr == "O":
		ai_next = "9"
	elif tr == "O" and br == "O":
		ai_next = "6"
	elif tr == "O" and bl == "O":
		ai_next = "5"
	elif ml == "O" and mm == "O":
		ai_next = "6"
	elif ml == "O" and mr == "O":
		ai_next = "5"
	elif ml == "O" and tl == "O":
		ai_next = "7"
	elif mm == "O" and tl == "O":
		ai_next = "7"
	elif mm == "O" and tm == "O":
		ai_next = "8"
	elif mm == "O" and tr == "O":
		ai_next = "7"
	elif mm == "O" and ml == "O":
		ai_next = "6"
	elif mm == "O" and mr == "O":
		ai_next = "4"
	elif mm == "O" and bl == "O":
		ai_next = "3"
	elif mm == "O" and bm == "O":
		ai_next = "2"
	elif mm == "O" and br == "O":
		ai_next = "1"
	elif mm == "O" and mr == "O":
		ai_next = "4"
	elif mm == "O" and br == "O":
		ai_next = "1"
	elif mr == "O" and mm == "O":
		ai_next = "4"
	elif mr == "O" and ml == "O":
		ai_next = "5"
	elif mr == "O" and tr == "O":
		ai_next = "9"
	elif mr == "O" and br == "O":
		ai_next = "3"
	elif bl == "O" and tl == "O":
		ai_next = "4"
	elif bl == "O" and tr == "O":
		ai_next = "5"
	elif bl == "O" and ml == "O":
		ai_next = "1"
	elif bl == "O" and mm == "O":
		ai_next = "3"
	elif bl == "O" and bm == "O":
		ai_next = "9"
	elif bl == "O" and br == "O":
		ai_next = "8"
	elif bm == "O" and tm == "O":
		ai_next = "5"
	elif bm == "O" and mm == "O":
		ai_next = "2"
	elif bm == "O" and bl == "O":
		ai_next = "9"
	elif bm == "O" and br == "O":
		ai_next = "7"
	elif br == "O" and tl == "O":
		ai_next = "5"
	elif br == "O" and tr == "O":
		ai_next = "6"
	elif br == "O" and mm == "O":
		ai_next = "1"
	elif br == "O" and mr == "O":
		ai_next = "3"
	elif br == "O" and bl == "O":
		ai_next = "8"
	elif br == "O" and bm == "O":
		ai_next = "7"
	else:
		return("null")
	return
def check_win_O():
	if tl == "X" and tm == "X" and tr == "X":
		return("player win")
	if tl == "X" and mm == "X" and br == "X":
		return("player win")
	if tl == "X" and ml == "X" and bl == "X":
		return("player win")
	if tl == "X" and tm == "X" and tr == "X":
		return("player win")
	if tm == "X" and mm == "X" and bm == "X":
		return("player win")
	if tr == "X" and mr == "X" and br == "X":
		return("player win")
	if tr == "X" and mm == "X" and bl == "X":
		return("player win")
	if ml == "X" and mm == "X" and mr == "X":
		return("player win")
	if tl == "O" and tm == "O" and tr == "O":
		return("computer win")
	if tl == "O" and mm == "O" and br == "O":
		return("computer win")
	if tl == "O" and ml == "O" and bl == "O":
		return("computer win")
	if tl == "O" and tm == "O" and tr == "O":
		return("computer win")
	if tm == "O" and mm == "O" and bm == "O":
		return("computer win")
	if tr == "O" and mr == "O" and br == "O":
		return("computer win")
	if tr == "O" and mm == "O" and bl == "O":
		return("computer win")
	if ml == "O" and mm == "O" and mr == "O":
		return("computer win")
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
#todo: check ai O 
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
	print(f"{tl}  |  {tm}  |  {tr}",flush=True)
	print(f"_____________",flush=True)
	print(f"{ml}  |  {mm}  |  {mr}",flush=True)
	print(f"_____________",flush=True)
	print(f"{bl}  |  {bm}  |  {br}",flush=True)
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
						if play_go == 1 and tl != " ":
							print("that is alredy taken")
						if play_go == 2 and tm != " ":
							print("that is alredy taken")
						if play_go == 3 and tr != " ":
							print("that is alredy taken")
						if play_go == 4 and ml != " ":
							print("that is alredy taken")
						if play_go == 5 and mm != " ":
							print("that is alredy taken")
						if play_go == 6 and mr != " ":
							print("that is alredy taken")
						if play_go == 7 and bl != " ":
							print("that is alredy taken")
						if play_go == 8 and bm != " ":
							print("that is alredy taken")
						if play_go == 9 and br != " ":
							print("that is alredy taken")
						else:
							if play_go == 1:
								tl = "O"
							if play_go == 2:
								tm = "O"
							if play_go == 3:
								tr = "O"
							if play_go == 4:
								ml = "O"
							if play_go == 5:
								mm = "O"
							if play_go == 6:
								tl = "O"
							if play_go == 7:
								tl = "O"
							if play_go == 8:
								tl = "O"
							if play_go == 9:
								tl = "O"
							break
					print_ui()
					if mm == "O":
						while True:
							rand = random.randint(1,9)
							if rand == 1 and tl == " ":
								tl = "X"
								break
							elif rand == 2 and tm == " ":
								tm = "X"
								break
							elif rand == 3 and tr == " ":
								tr = "X"
								break
							elif rand == 4 and ml == " ":
								ml = "X"
								break
							if rand == 5 and mm == " ":
								mm = "X"
								break
							elif rand == 6 and mr == " ":
								mr = "X"
								break
							elif rand == 7 and bl == " ":
								bl = "X"
								break
							elif rand == 8 and bm == " ":
								bm = "X"
								break
							elif rand == 9 and br == " ":
								br = "X"
								break
						print_ui()
	elif play == 2:
		redyplayerone = input("who is player 1: ")
		redyplayertwo = input("who is player 2: ")
	else:
		print("sorry i didn't understand")