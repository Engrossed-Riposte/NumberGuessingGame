#!/bin/python3
import random

top_of_range = input("Type a number ")
guesses = 0



if top_of_range.isdigit():
	top_of_range = int(top_of_range)
	if top_of_range <= 0:
		print("Please enter a number larger than 0 ")
		quit()
else:
	print("Please enter a number next time")




random_number = random.randint(0, top_of_range)

while True:
	guesses += 1
	user_guess = input("Make a guess ")

	if user_guess.isdigit():
		user_guess = int(user_guess)
	else:
		print("Please enter a number next time")
		continue

	if user_guess > random_number:
			print("You guessed above the number!")
	elif user_guess < random_number:
		 print("You are below the number!")
	
	

	if user_guess == random_number:
		print("You got it! ")
		break
	else:
		print("You got it wrong.... try again ")
		continue
	
	

print("You figured it out in", guesses, "guesses")
