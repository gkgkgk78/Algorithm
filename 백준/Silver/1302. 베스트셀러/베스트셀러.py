n=int(input().rstrip())
dic={}
for i in range(n):
    e=input().rstrip()
    if e not in dic:
        dic[e]=1
    else:
        dic[e]+=1

aa=max(dic.values())
re=[]
for e,a in dic.items():
    if a==aa:
        re.append(e)
re.sort()
print(re[0])