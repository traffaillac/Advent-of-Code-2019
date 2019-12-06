import sys

graph = {}
for l in sys.stdin:
	a, b = l.rstrip().split(')')
	graph.setdefault(a, [None, [], False])
	graph.setdefault(b, [None, [], False])
	graph[a][1].append(b)
	graph[b][0] = a

def count_orbits(a, d):
	return d + sum(count_orbits(b, d + 1) for b in graph[a][1])
print(count_orbits('COM', 0))

dfs = [('YOU', 0)]
while dfs[0][0] != 'SAN':
	a, n = dfs.pop(0)
	p, c, v = graph[a]
	if not v:
		graph[a][2] = True
		if p != None:
			dfs.append((p, n + 1))
		for b in c:
			dfs.append((b, n + 1))
print(dfs[0][1] - 2)
