from itertools import count

# pos = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
pos = ([8, 0, 8], [0, -5, -10], [16, 10, -5], [19, -10, -7])
vel = ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0])
explored = [{} for _ in range(3)]
for steps in count():
	for i in range(3):
		if explored[i] != None:
			s = explored[i].setdefault(tuple(p[i] for p in pos) + tuple(v[i] for v in vel), steps)
			if s != steps:
				print(f'{i}: {steps} repeats {s}')
				explored[i] = None
	
	for m in range(4):
		for n in range(4):
			for i in range(3):
				vel[m][i] += min(max(pos[n][i] - pos[m][i], -1), 1)
	for m in range(4):
		for i in range(3):
			pos[m][i] += vel[m][i]
print(sum(sum(abs(p) for p in pos[m]) * sum(abs(v) for v in vel[m]) for m in range(4)))
