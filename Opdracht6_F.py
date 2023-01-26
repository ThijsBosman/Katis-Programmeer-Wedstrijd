N, t = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

flag = True

if(t == 1):
	for x in range(len(A) - 1):
		for y in range(x + 1, len(A)):
			if(A[x] + A[y] == 7777):
				print("Yes")
				flag = False
				break
		else: continue
		break
		
	if(flag): print("No")

if(t == 2):
	for x in range(len(A) - 1):
		for y in range(x + 1, len(A)):
			if(A[x] == A[y]):
				print("Contains duplicate")
				flag = False
				break
		else: continue
		break
		
	if(flag): print("Unique")

if(t == 3):
	total_count = 0
	for unique_value in set(A):
		if(total_count > N / 2): break
		
		count = A.count(unique_value)
		if(count > N / 2):
			print(unique_value)
			flag = False
			break
		total_count += count
		A = [i for i in A if i != unique_value]

	if(flag): print(-1)

if(t == 4):
	A = sorted(A)

	if(len(A) % 2 == 0): print(A[int(len(A) / 2) - 1], A[int(len(A) / 2)])
	else: print(A[int((len(A) - 1) / 2)])

else:
	print(*set(sorted([x for x in A if (x >= 100 and x < 1000)])))
