from utils import type_text
from config import *
def changeSettings():
	while True:
		type_text("ok")
		type_text("0 to go back to the terminal")
		type_text(f"1 to toggle typing: {typing}")
		type_text(f"2 to toggle debugging: {debugging}")
		imp = input("what do you want")
		if imp == 0:
			type_text("ok back to the terminal")
			break
		elif imp == 1:
			typing = not typing
		elif imp == 2:
			debugging = not debugging