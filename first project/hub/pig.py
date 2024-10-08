from config import debugging
from utils import type_text
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
		type_text(out)
def call():
	type_text("Hi i am Pig")
	last_bit()
call()