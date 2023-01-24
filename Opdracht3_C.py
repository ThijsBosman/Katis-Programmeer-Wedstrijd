coords = []

for i in range(3):
	vals = input().split(" ")
	coords.append((int(vals[0]), int(vals[1])))

def disctance_square(coord1, coord2):
	return (coord1[0] - coord2[0]) * (coord1[0] - coord2[0]) + (coord1[1] - coord2[1]) * (coord1[1] - coord2[1])

dist1 = []
for i in range(1,3):
	dist1.append(disctance_square(coords[0], coords[i]))

dist2 = []
dist2.append(disctance_square(coords[1], coords[0]))
dist2.append(disctance_square(coords[1], coords[2]))

x_missing = 0
y_missing = 0

# coord 0 is corner
if(dist1[0] == dist1[1]):
	x_missing = coords[1][0] + (coords[2][0] - coords[0][0])
	y_missing = coords[1][1] + (coords[2][1] - coords[0][1])

# Coord 1 i corner
elif(dist2[0] == dist2[1]):
	x_missing = coords[0][0] + (coords[2][0] - coords[1][0])
	y_missing = coords[0][1] + (coords[2][1] - coords[1][1])

else:
	x_missing = coords[0][0] + (coords[1][0] - coords[2][0])
	y_missing = coords[0][1] + (coords[1][1] - coords[2][1])

print(x_missing, y_missing)
