def pig(transalte):
	iteration = 1
	output = ""
	test = ""
	inputs = transalte
	if len(inputs)<3:
		return(inputs)
	for i in inputs:
		if i == "a":
			break
		if i == "e":
			break
		if i == "i":
			break
		if i == "o":
			break
		if i == "u":
			break
		if i == "y"and iteration > 1:
			break
		iteration =+ 1
		output = output + i
	inputs =  inputs[iteration:]
	output = output + inputs + "ay"
	return(output)

print(pig(input(":")))