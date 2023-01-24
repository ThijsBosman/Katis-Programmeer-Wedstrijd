placement = [input() for i in range(5)]

knight_coords = []

def abs(x):
	return x if x >= 0 else -x

for row in range(5):
	pieces = [*placement[row]]
	for column in range(5):
		if(pieces[column] == 'k'):
			knight_coords.append((row, column))

flag = True

if(len(knight_coords) != 9):
	print("invalid")
	flag = False
else:
	for knight1 in knight_coords:
		for knight2 in knight_coords:
			if(knight1 == knight2):
				continue

			delta_x = abs(knight1[0] - knight2[0])
			delta_y = abs(knight1[1] - knight2[1])

			if(((delta_x == 1 and delta_y == 2) or (delta_x == 2 and delta_y == 1)) and flag):
				print("invalid")
				flag = False
				break

if(flag):
	print("valid")
