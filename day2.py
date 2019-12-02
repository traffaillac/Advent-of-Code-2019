ref = [int(i) for i in input().split(',')]
for noun in range(100):
	for verb in range(100):
		mem = ref.copy()
		mem[1] = noun
		mem[2] = verb
		ip = 0
		while mem[ip] != 99:
			if mem[ip] == 1:
				mem[mem[ip + 3]] = mem[mem[ip + 1]] + mem[mem[ip + 2]]
			elif mem[ip] == 2:
				mem[mem[ip + 3]] = mem[mem[ip + 1]] * mem[mem[ip + 2]]
			ip += 4
		if mem[0] == 19690720:
			print(100 * noun + verb)
