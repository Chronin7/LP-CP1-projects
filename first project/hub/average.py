from utils import type_text
from config import debugging
def run(classes):
	type_text("I am AV the Avenger.")
	while True:
		runs = 1
		list_o_nums = []
		percentage = 0
		classes = input("How many things do you want to average or type stop to stop: ")
		if classes == "stop":
			type_text("ok sending you back to Hubby")
			break
		classes = int(classes)
		for x in range(classes):
			one_at_a_time = int(input(f"what is the percentage of # {runs} (only numbers please): "))
			percentage += one_at_a_time
			list_o_nums.append(one_at_a_time)
			runs += 1
		type_text(f"you entered {list_o_nums} #'s it is an average of {percentage/classes}")
		go_agin = input("do you want to use again (y/n): ")
		if go_agin == "n":
			type_text("ok sending you back to Hubby")
			break
