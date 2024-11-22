num = 0
var = ""
lists = []
while True:
	try:
		num = int(input("how many nums in the list: "))
		break
	except:
		print("enter a number")
for x in range(num):
	while True:
		try:
			lists.append(int(input(f"what is #{x+1}: ")))
			break
		except:
			print("please enter a number")
for x in range(num):
	var = ""
	for i in range(lists[x]):
		var+="*"
	print(f"{x+1}: {var}")