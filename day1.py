import sys
res = 0
for l in sys.stdin:
	fuel = int(l) // 3 - 2
	while fuel > 0:
		res += fuel
		fuel = fuel // 3 - 2
print(res)
