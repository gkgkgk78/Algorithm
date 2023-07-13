import sys

input = sys.stdin.readline
n = int(input().rstrip())
mindp = [0] * (3)
maxdp = [0] * (3)
nmindp = [0] * (3)
nmaxdp = [0] * (3)
e = list(map(int, input().split()))
for i in range(3):
    mindp[i] = e[i]
    maxdp[i] = e[i]

for i in range(1, n):
    e = list(map(int, input().split()))
    nmindp[0] = min(mindp[0], mindp[1]) + e[0]
    nmaxdp[0] = max(maxdp[0], maxdp[1]) + e[0]
    nmindp[1] = min(mindp[0], mindp[1], mindp[2]) + e[1]
    nmaxdp[1] = max(maxdp[0], maxdp[1], maxdp[2]) + e[1]
    nmindp[2] = min(mindp[1], mindp[2]) + e[2]
    nmaxdp[2] = max(maxdp[1], maxdp[2]) + e[2]

    for j in range(3):
        mindp[j] = nmindp[j]
        maxdp[j] = nmaxdp[j]

minz = min(mindp[0], mindp[1], mindp[2])
maxz = max(maxdp[0], maxdp[1], maxdp[2])
print(maxz, minz)