n = input()
byte_data = [int(x) for x in input().split(" ")]

def unscramble(val):
	bits = []

	# bit 0
	bits.append(val & 1)

	for i in range(1,8):
		bits.append(((val >> i) & 1) ^ bits[i-1])


	unscramled_val = 0
	for i in range(len(bits)):
		unscramled_val |= bits[i] << i

	return unscramled_val




byte_data = [unscramble(x) for x in byte_data]
print(' '.join(map(str, byte_data)))
