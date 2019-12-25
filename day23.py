from collections.abc import Iterable
from sys import stdin

def run(prog, input=[]):
	mem = prog[:]
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
queues = [[i] for i in range(50)]
computers = [run(prog[:] + [0]*100000, queues[i]) for i in range(50)]
for i in range(50):
	next(computers[i])
wait = list(range(50))
last = 0
while True:
	while wait:
		i = wait.pop(0)
		print(f'i={i}')
		while True:
			dst, X, Y = computers[i].send(-1), next(computers[i]), next(computers[i])
			if dst == None:
				break
			print(dst, X, Y)
			if dst == 255:
				nat = (X, Y)
			else:
				queues[dst].extend((X, Y))
				if not dst in wait:
					wait.append(dst)
	if nat[1] == last:
		print(last)
		break
	last = nat[1]
	queues[0].extend(nat)
	wait.append(0)
