import sys
input = sys.stdin.readline
a,b=map(int,input().split())
def get_prime(x):
	la = []
	ee = (int)(x + 1)
	is_prime = [1] * (ee)
	for i in range(2, ee):
		start = i + i
		if is_prime[i] == 1:
			la.append(i)
			while start < ee:
				is_prime[start] = 0
				start += i
	return la
aa=get_prime(b)

for i in aa:
	if i>=a:
		print(i)