n=int(input().rstrip())
want=[]
for i in range(n):
    l=input().rstrip()
    want.append(l)
want=sorted(want,key=lambda x:len(x))

remove=[]

for k in range(len(want)):
    g=list(want[k])
    for j in range(k+1,len(want)):
        if len(want[k])<=len(want[j]):
            if k!=j:
                e=list(want[j])
                if e[0:len(want[k])]==g:
                    remove.append(want[k])
                    break
print(len(want)-len(remove))