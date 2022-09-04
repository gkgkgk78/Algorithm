a = input().split('-')
num = []

for i in a:
    cnt=0
    s=i.split('+')
    for j in s:
        cnt=cnt+int(j)
    num.append(cnt)
sum=num[0]
for i in range(1,len(num)):
    sum=sum-num[i]
print(sum)