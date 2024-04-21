#!/bin/python3

import random
import string

def generate_password():
	letters = string.ascii_letters
	numbers = string.digits
	symbols = string.punctuation

	print("=" * 50)
	print("Password Generator")
	print("=" * 50)

	pwstr = input("What kind of password do you want? strong, medium or weak?: ")
	pwstr = pwstr.lower()
	
	if pwstr == "strong":
		pw = ((random.choices(letters, k=8)) + (random.choices(numbers, k=4)) + (random.choices(symbols, k=3)))
		random.shuffle(pw)
		spw = "".join(pw)
		print(f"Your {pwstr} password is: {spw}")
	
	elif pwstr == "medium":
		pw = ((random.choices(letters, k=6)) + (random.choices(numbers, k=4)))
		random.shuffle(pw)
		mpw = "".join(pw)
		print(f"Your {pwstr} password is: {mpw}")
	elif pwstr == "weak":
		pw = (random.choices(letters, k=7))
		random.shuffle(pw)
		wpw = "".join(pw)
		print(f"Your {pwstr} password is: {wpw}")
	else:
		print("=" * 50)
		print("Incorrect format!")
		print("Please type strong, medium or weak!")
		print("=" * 50)

while True:
	generate_password()
	another_password = input("Do you want to generate another password? yes/no: ")
	if another_password.lower() != "yes":
		print("Exiting...")
		break
