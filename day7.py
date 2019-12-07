import itertools

def run(mem, ip, input, output):
	while mem[ip] != 99:
		inst, a, b, c = mem[ip:ip+4]
		op, ra, rb = inst % 100, a if inst // 100 % 10 else mem[a], b if inst // 1000 or not 0 <= b < len(mem) else mem[b]
		if op == 1:
			mem[c] = ra + rb
			ip += 4
		elif op == 2:
			mem[c] = ra * rb
			ip += 4
		elif op == 3:
			if not input:
				return ip
			mem[a] = input.pop(0)
			ip += 2
		elif op == 4:
			output.append(ra)
			ip += 2
		elif op == 5:
			ip = rb if ra else ip + 3
		elif op == 6:
			ip = ip + 3 if ra else rb
		elif op == 7:
			mem[c] = 1 if ra < rb else 0
			ip += 4
		elif op == 8:
			mem[c] = 1 if ra == rb else 0
			ip += 4
	return -1

with open('tmp.in') as f:
	prog = [int(i) for i in f.read().split(',')] + [0]
largest = 0
for p in itertools.permutations([5, 6, 7, 8, 9]):
	print(p)
	mems = tuple(prog.copy() for _ in range(5))
	ips = [0] * 5
	inputs = tuple([i] for i in p)
	inputs[0].append(0)
	cur = 0
	while ips[4] >= 0:
		ips[cur] = run(mems[cur], ips[cur], inputs[cur], inputs[(cur + 1) % 5])
		cur = (cur + 1) % 5
	largest = max(largest, inputs[0][-1])
print(largest)
