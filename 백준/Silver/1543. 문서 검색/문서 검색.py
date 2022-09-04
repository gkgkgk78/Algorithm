a=input()
b=input()
count=0
idx=0
for i in range(0,len(a)):
    if idx>i:
        continue
    t=a[i:i+len(b)]
    if t==b:
        count+=1
        idx=i+len(b)

print(count)