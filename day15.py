from collections.abc import Iterable
from sys import stdin

def run(prog, input=[]):
	mem = prog + [0] * 1_000_000
	ip = 0
	base = 0
	while mem[ip] != 99:
		inst, a, b, c = mem[ip:ip+4]
		op, ma, mb, mc = inst % 100, inst // 100 % 10, inst // 1000 % 10, inst // 10000
		ra = a if ma == 1 else mem[a] if ma == 0 else mem[base + a]
		rb = b if mb == 1 else mem[b] if mb == 0 else mem[base + b]
		wa = a if ma == 0 else base + a
		wc = c if mc == 0 else base + c
		if op == 1:
			mem[wc] = ra + rb
			ip += 4
		elif op == 2:
			mem[wc] = ra * rb
			ip += 4
		elif op == 3:
			while not input:
				v = yield
				input.extend(v if isinstance(v, Iterable) else (v,) if isinstance(v, int) else ())
			mem[wa] = input.pop(0)
			assert mem[wa] != None
			ip += 2
		elif op == 4:
			v = yield ra
			input.extend(v if isinstance(v, Iterable) else (v,) if isinstance(v, int) else ())
			ip += 2
		elif op == 5:
			ip = rb if ra else ip + 3
		elif op == 6:
			ip = ip + 3 if ra else rb
		elif op == 7:
			mem[wc] = 1 if ra < rb else 0
			ip += 4
		elif op == 8:
			mem[wc] = 1 if ra == rb else 0
			ip += 4
		elif op == 9:
			base += ra
			ip += 2

prog = [int(i) for i in stdin.read().split(',')]
droid = run(prog)
next(droid)
grid = [[' '] * 50 for _ in range(50)]

def explore(x, y, tile):
	grid[y][x] = tile
	dist = 0 if tile == 'o' else 1000000
	for d, (dx, dy) in enumerate(((0, -1), (0, 1), (-1, 0), (1, 0))):
		if grid[y + dy][x + dx] == ' ':
			status = droid.send(d + 1)
			if status == 0:
				grid[y + dy][x + dx] = '#'
			else:
				if status == 2: print(f'oxygen system at {x+dx}, {y+dy}')
				dist = min(dist, 1 + explore(x + dx, y + dy, 'o' if status == 2 else '.'))
				droid.send((d ^ 1) + 1)
	return dist

print(explore(len(grid[0]) // 2, len(grid) // 2, '.'))
print('\n'.join(''.join(l) for l in grid))

bfs = [(0, 9, 11)]
while bfs:
	minutes, x, y = bfs.pop(0)
	for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
		if grid[y+dy][x+dx] == '.':
			grid[y+dy][x+dx] = 'o'
			bfs.append((minutes+1, x+dx, y+dy))
print(minutes)
