from heapq import heappush, heappop, heapify
from sys import stdin, exit

# grid should be modified by hand bofore
grid = stdin.read().split()
adj = ((0,-1), (1,0), (0,1), (-1,0))
N = sum(97 <= ord(c) <= 122 for l in grid for c in l)
x0, y0 = [(x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '@'][0]

def nb(x, y):
	edges = [None] * N
	visited = [[False] * len(l) for l in grid]
	bfs = [(0, x, y, 0)]
	while bfs:
		steps, x, y, doors = bfs.pop(0)
		if visited[y][x]: continue
		visited[y][x] = True
		c = ord(grid[y][x])
		if 65 <= c <= 90:
			doors |= 1 << (c - 65)
		elif 97 <= c <= 122:
			edges[c - 97] = (steps, doors)
		for dx, dy in adj:
			if grid[y+dy][x+dx] != '#' and not visited[y+dy][x+dx]:
				bfs.append((steps+1, x+dx, y+dy, doors))
	return edges

graph = [None] * N
for y in range(len(grid)):
	for x in range(len(grid[y])):
		c = ord(grid[y][x])
		if 97 <= c <= 122:
			graph[c - 97] = nb(x, y)
for x, y in ((x0,y0), (x0+2,y0), (x0,y0+2), (x0+2,y0+2)):
	graph.append(nb(x, y))

visited = set()
heap = [(0, 0, [N, N+1, N+2, N+3])]
while heap:
	path, keys, pos = heappop(heap)
	conf = (keys, *pos)
	if conf in visited: continue
	visited.add(conf)
	if keys == (1 << N) - 1: break
	for r, p in enumerate(pos):
		for c, n in enumerate(graph[p]):
			if n and keys & 1 << c == 0 and keys & n[1] == n[1]:
				new = pos[:]
				new[r] = c
				heappush(heap, (path + n[0], keys | 1 << c, new))
print(path)
