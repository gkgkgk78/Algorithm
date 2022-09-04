n=int(input().rstrip())
# s g p d
mvp=list(map(int ,input().split()))
slsl=input()
sum=0
grid=[0]* n
total=0

for i in slsl:
    if i=='B': #0
        if total==0:
            grid[total]=mvp[0]-1
            total+=1
        else:
            le = mvp[0] - grid[total - 1] - 1
            grid[total] = le
            total += 1
    elif i=='S':#1
        le=mvp[1]-grid[total-1]-1
        grid[total]=le
        total+=1
    elif i == 'G':#2
        le = mvp[2] - grid[total - 1] - 1
        grid[total] = le
        total += 1
    elif i == 'P':#3
        le = mvp[3] - grid[total - 1] - 1
        grid[total] = le
        total += 1
    elif i == 'D':
        grid[total] = mvp[3]
        total += 1

sums=0
for i in grid:
    sums+=i
print(sums)