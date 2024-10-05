import time
import random
from config import typing

def type_text(te):
	if typing:
		for c in str(te):
			print(c, end = "", flush = True)
			time.sleep(random.uniform(.01,.1))
		print("")
	else:
		print(te)