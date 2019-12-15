from sys import stdin

tree = {'ORE': (1, {})}
for l in stdin:
	inputs, res = l.split('=>')
	n, output = res.split()
	tree[output] = (int(n), {i.split()[1]:int(i.split()[0]) for i in inputs.split(',')})

toposort = {'ORE': 0} # dict keeps insertion order
it = iter(tree.items())
while len(toposort) < len(tree):
	try:
		chem, (n, inputs) = next(it)
	except:
		it = iter(tree.items())
		chem, (n, inputs) = next(it)
	if not chem in toposort and toposort.keys() >= inputs.keys():
		toposort[chem] = 0

def ore(fuel):
	for chem in toposort:
		toposort[chem] = fuel if chem == 'FUEL' else 0
	for chem in reversed(tuple(toposort.keys())):
		n, inputs = tree[chem]
		times = (toposort[chem] + n - 1) // n
		for raw, m in inputs.items():
			toposort[raw] += m * times
	return toposort['ORE']

print(ore(1))
a, b = 1, 1000000000000
while a < b:
	c = (a + b + 1) // 2
	if ore(c) > 1000000000000:
		b = c - 1
	else:
		a = c
print(a)
