om = int(input("how many lists are in the list of lists: "))
omg = []
for e in range(om):
	ou = []
	for x in input("""what is the list (note "hi jpl" would come out as ["h","i"," ","j","p","l"]): """):
		ou.append(x)
	omg.append(ou)
eee = input("what do you want to count across all lists: ")
eeeeee = 0
for x in omg:
	eeeeee += list(x).count(eee)
print(eeeeee)