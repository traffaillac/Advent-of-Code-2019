def wire():
	h, v = [], []
	x, y, s = 0, 0, 0
	for inst in input().split(','):
		d, i = inst[0], int(inst[1:])
		if d == 'R':
			h.append((x, y, x + i, s))
			x += i
		elif d == 'U':
			v.append((x, y, y + i, s))
			y += i
		elif d == 'L':
			h.append((x, y, x - i, s))
			x -= i
		elif d == 'D':
			v.append((x, y, y - i, s))
			y -= i
		s += i
	return h, v

def intersections(h, v):
	i = []
	for x0, y, x1, sh in h:
		for x, y0, y1, sv in v:
			if min(x0, x1) < x < max(x0, x1) and min(y0, y1) < y < max(y0, y1):
				i.append((sh + abs(x - x0) + sv + abs(y - y0), x, y))
	return i

h1, v1 = wire()
h2, v2 = wire()
i = intersections(h1, v2) + intersections(h2, v1)
print(sorted(i))
