from itertools import count
from math import gcd, atan2, pi, hypot
from sys import stdin

grid = stdin.read().split()
asteroids = {(x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '#'}
best = (0, 0, 0)
for x, y in asteroids:
	seen = -1
	for i, j in asteroids:
		d = gcd(abs(i - x), abs(j - y))
		seen += 0 if any((x+(i-x)//d*k, y+(j-y)//d*k) in asteroids for k in range(1, d)) else 1
	best = max(best, (seen, x, y))
print(best[0])

_, x, y = best
asteroids.remove((x, y))
targets = [(atan2(x-i, j-y), hypot(i-x, j-y), i-x, j-y) for i, j in asteroids]
for t, (a, h, i, j) in enumerate(targets):
	if i == 0 and j < 0:
		targets[t] = -pi, h, i, j
targets.sort()
print('\n'.join(map(str, targets)))
t = 0
for vap in range(1, 201):
	a, _, i, j = targets.pop(t)
	print(vap, x+i, y+j)
	t = next((u for u in range(t, len(targets)) if targets[u][0] > a), 0)
