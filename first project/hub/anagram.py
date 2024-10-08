import random
from utils import type_text
from config import debugging
def anagram(word):
	type_text("Hi i am Anny")
	while True:
		anagram = []
		output = ""
		doit = "12345"
		word = input("what is the word that you want into anagram or type stop to stop: ")
		if word == "stop":
			type_text("sending you back to Hubby")
			break
		if word == "":
			type_text("oops looks like you are a bit trigerhappy")
		else:
			rand = len(word)
			for y in doit:
				output = ""
				anagram = []
				for x in word:
					anagram.insert(random.randint(1,rand),x)
				for i in anagram:
					output = output + i
				print (output)
