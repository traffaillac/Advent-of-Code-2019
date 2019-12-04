count = 0
for p in range(171309, 643604):
	s = str(p)
	if any(adj[0] in s and not adj[1] in s for adj in [('22', '222'), ('33', '333'), ('44', '444'), ('55', '555'), ('66', '666'), ('77', '777'), ('88', '888'), ('99', '999')]) and list(s) == sorted(s):
		count += 1
print(count)
