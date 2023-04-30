f = open('64211_32831368966369104_doc (1).txt', 'r')
n = [int(x) for x in f]
l=len(n)-1
k=0
m=0
for i in range(l+1):
    if n[i]%7==0:
        m=max(m,n[i])
for i in range(l):
    if (n[i]%7==0 or n[i+1]%7==0) and n[i]+n[i+1]<=m:
        k+=1
print(k)