import itertools

def run(prog, input):
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
			mem[wa] = input.pop(0)
			ip += 2
		elif op == 4:
			v = yield ra
			if v: input.extend(v)
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

with open('tmp.in') as f:
	prog = [int(i) for i in f.read().split(',')]
for i in run(prog, [2]):
	print(i)
