from random import randint

def generate_letter():
	number = randint(1, 26)
	if number == 1:
		return 'A'
	elif number == 2:
		return 'B'
	elif number == 3:
		return 'C'
	elif number == 4:
		return 'D'
	elif number == 5:
		return 'E'
	elif number == 6:
		return 'F'
	elif number == 7:
		return 'G'
	elif number == 8:
		return 'H'
	elif number == 9:
		return 'I'
	elif number == 10:
		return 'J'
	elif number == 11:
		return 'K'
	elif number == 12:
		return 'L'
	elif number == 13:
		return 'M'
	elif number == 14:
		return 'N'
	elif number == 15:
		return 'O'
	elif number == 16:
		return 'P'
	elif number == 17:
		return 'Q'
	elif number == 18:
		return 'R'
	elif number == 19:
		return 'S'
	elif number == 20:
		return 'T'
	elif number == 21:
		return 'U'
	elif number == 22:
		return 'V'
	elif number == 23:
		return 'W'
	elif number == 24:
		return 'X'
	elif number == 25:
		return 'Y'
	elif number == 26:
		return 'Z'

names = list()
for _ in range(200-15):
	names.append(generate_letter() + generate_letter() + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + '-' + generate_letter() + generate_letter())