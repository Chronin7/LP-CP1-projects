while True:
	runs = 1
	percentage = {}
	classes = input("I am AV the Avenger. How many things do you want to average or type stop to stop: ")
	if classes == "":
		print("oops looks like you are a bit trigerhappy")
	else:
		if classes == "stop":
			print("ok sending you back to Hubby")
			break
		for x in classes:
			one_at_a_time = int(input(f"what is the percentage of # {runs} (only numbers please): "))
			percentage =+ one_at_a_time
			runs =+ 1
		if 80 < percentage/classes:
			print(f"you entered {classes} #'s it is an average of {percentage/classes}%")
		else:
			print(f"you entered {classes} #'s it is an average of {percentage/classes}%")
		go_agin = input("do you want to use again (y/n): ")
		if go_agin == "n":
			break
