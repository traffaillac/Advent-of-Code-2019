from sys import stdin, exit

adj = ((0,-1), (-1,0), (1,0), (0,1))
grid = stdin.read().split('\n')
W, H = len(grid[0]), len(grid)

portals = {}
teleport = {}
for y in range(2, H-2):
	for x in range(2, W-2):
		if grid[y][x] != '.': continue
		d = min(x, W-x, y, H-y)
		for A, a in ((grid[y-2][x], grid[y-1][x]), (grid[y][x-2], grid[y][x-1]), (grid[y][x+1], grid[y][x+2]), (grid[y+1][x], grid[y+2][x])):
			if A.isalpha() and a.isalpha():
				X, Y = portals.setdefault(A+a, (x, y))
				if (X, Y) != (x, y):
					D = 1 if min(X, W-X, Y, H-Y) < d else -1
					teleport[(x, y)] = (A+a, X, Y, D)
					teleport[(X, Y)] = (A+a, x, y, -D)

bfs = [(*portals['AA'], 0)]
steps = [[[-1] * len(l) for l in grid] for d in range(200)]
steps[0][bfs[0][1]][bfs[0][0]] = 0
while bfs[0] != (*portals['ZZ'], 0):
	X, Y, D = bfs.pop(0)
	for x, y in map(lambda p:(X+p[0], Y+p[1]), adj):
		if grid[y][x] == '.' and steps[D][y][x] < 0:
			steps[D][y][x] = steps[D][Y][X] + 1
			bfs.append((x, y, D))
	assert D < len(steps)-1
	try:
		portal, x, y, d = teleport[(X, Y)]
		if D+d >= 0 and steps[D+d][y][x] < 0:
			# print(f'Teleport to level {D+d} through {portal} after {steps[D][Y][X]} steps')
			steps[D+d][y][x] = steps[D][Y][X] + 1
			bfs.append((x, y, D+d))
	except: pass
x, y = portals['ZZ']
print(steps[0][y][x])
