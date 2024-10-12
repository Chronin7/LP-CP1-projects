num = int(input("how many classes do you have:"))
listt = []
itera = 0
while num > itera:
	itera += 1
	listt.append(input(f"what is class #{itera}: "))
itera = 0
for x in listt:
	itera += 1
	print(f"period {itera}: {x}")