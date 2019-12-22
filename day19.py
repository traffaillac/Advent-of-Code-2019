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

prog = [int(i) for i in stdin.read().split(',')] + [0] * 100000
# print(sum(next(run(prog, [x, y])) for x in range(50) for y in range(50)))
# y=0.811x and y=0.925x
# a+b=1.736 and b-a=0.114
# x=99.(1+a)/(b-a) -> 1573
# y=99.a.(1+b)/(b-a) -> 1356
for y in range(1348, 1448):
	print(y, ''.join(('#' if next(run(prog, [x, y])) else '.' for x in range(1564, 1664))))
