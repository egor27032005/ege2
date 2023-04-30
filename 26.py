file=open('26.txt', 'r')
s=int(file.readline())
iabl=[[int(t) for t in x.strip().split()]for x in file]
iabl.sort()
maxI=0
maxK=0
for i in range(s-1):
    if iabl[i][0]==iabl[i+1][0]:
        r=iabl[i+1][1]-iabl[i][1]
        if r>maxK and i>maxI:
            maxK=r
            maxI=i
print(maxI,maxK-1)
##18814 98902