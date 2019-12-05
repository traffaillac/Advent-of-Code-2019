with open('tmp.in') as f:
	mem = [int(i) for i in f.read().split(',')] + [0]
ip = 0
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
		mem[a] = int(input())
		ip += 2
	elif op == 4:
		print(ra)
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
