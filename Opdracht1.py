n = int(input())
result = []

for i in range(n):
	result.append(input())

correct = 0

for i in range(len(result) - 1):
	correct += result[i] == result[i + 1]

print(correct)
