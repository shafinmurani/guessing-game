#!/bin/python3

import random

def guess(x):
	random_number = random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Guess number between 1 and {x}\n'))
		if guess < random_number:
			print("Too low.")
		elif guess > random_number:
			print("Too high.")
	print(f"Congratlations you guessed the corect nmumber.{random_number}!!!")
guess(random.randint(1,99))
