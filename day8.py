str = input()
W, H, L = 25, 6, len(str) // 150
layers = [str[i:i+W*H] for i in range(0, len(str), W*H)]
l = sorted((sum(d is '0' for d in layers[i]), i) for i in range(L))[0][1]
print(sum(d is '1' for d in layers[l]) * sum(d is '2' for d in layers[l]))
for d in range(W * H):
	print(next(layers[i][d] for i in range(L) if layers[i][d] is not '2'), end='')
