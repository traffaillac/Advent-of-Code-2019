from sys import stdin, exit

# x = (A*x+B) % N
A, B, N, M = 1, 0, 119315717514047, 101741582076661
for l in stdin:
	w = l.split()
	if w[1] == 'into': # deal into new stack -> N-1-(A*x+B)
		A = -A%N
		B = N-1-B
	elif w[0] == 'cut': # cut C -> (A*x+B)-C
		B = (B-int(w[1]))%N
	else: # deal with increment I -> (A*x+B)*I
		A = (A*int(w[3]))%N
		B = (B*int(w[3]))%N
print(f'{A}x+{B} for one shuffle')

# (A*x+B)^M
C, D = 1, 0
while M > 0:
	if M & 1: # A*(C*x+D)+B
		C = A*C%N
		D = (A*D+B)%N
	B = (A*B+B)%N
	A = A*A%N
	M >>= 1
print(f'{C}x+{D} for all shuffles')

# C*x+D=y -> E*y+F=x
E = pow(C, N-2, N)
F = (-D*E) % N
print(f'{E}x+{F} to revert all shuffles')
print((E*2020+F)%N)
