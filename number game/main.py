import random 
loops = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
num = random.randint(1, 100)
print ("Welcome to GUESS THE NUMBER. You have 20 attempts to get the number then you lose. Good luck!")
guess = int (input("guess from 1-100: "))
for x in loops:
	
	if guess == num: 
		print ("you got it! Game Over")
		break
	if guess > num:
		guess = int (input("Its smaller: "))
	if guess < num:
		guess = int (input("its bigger: "))
	if x ==20:
		print ("game over")
		break
