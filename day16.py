from itertools import accumulate

message = input()
partial = ([int(i) for i in message] * 10000)[int(message[:7]):]
for p in range(100):
	print(p)
	for i in range(len(partial)-2, -1, -1):
		partial[i] = (partial[i] + partial[i+1]) % 10
print(''.join(map(str, partial[:8])))

# for i in range(100):
# 	sums = [0] + list(accumulate(pattern))
# 	copy = [0] * len(pattern)
# 	for j in range(len(copy)):
# 		s = 0
# 		for k in range(j, len(copy), (j+1)*4):
# 			s += sums[min(k+j+1, len(copy))] - sums[k]
# 		for k in range(2+j*3, len(copy), (j+1)*4):
# 			s -= sums[min(k+j+1, len(copy))] - sums[k]
# 		copy[j] = s % 10 if s >= 0 else -s % 10
# 	pattern = copy
# print(''.join(map(str, pattern[:8])))
