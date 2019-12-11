from sys import stdin

def run(prog):
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
			mem[wa] = yield
			assert mem[wa] != None
			ip += 2
		elif op == 4:
			yield ra
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

steps = ((0, -1), (1, 0), (0, 1), (-1, 0))
prog = [int(i) for i in stdin.read().split(',')]
W = 100
grid = [[' '] * W for _ in range(W)]
x, y, d = W // 2, W // 2, 0
grid[y][x] = '#'
robot = run(prog)
try:
	while True:
		next(robot)
		grid[y][x] = '#' if robot.send(1 if grid[y][x] == '#' else 0) else '.'
		d = (d + next(robot) * 2 + 3) % 4
		x += steps[d][0]
		y += steps[d][1]
except: print('\n'.join(''.join(l) for l in grid))
print(sum(l.count('#') + l.count('.') for l in grid))
