

n=input()
sum=0
count0=0
count1=0
if n[0]=='0':
    count0+=1
else:
    count1+=1
for i in range(len(n)-1):
    if n[i]!=n[i+1]:
        if n[i+1]=='1':
            count1+=1
        else:
            count0+=1
print(min(count0,count1))





