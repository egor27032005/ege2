k=0
for x in range(150000,200001):
    k=0
    for y in range(2,x//2+1):
        if x%y==0:
            k+=1
            z=y
    if k==48:
        print(z)