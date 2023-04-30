file = open('2266.txt')
N=file.readline()
arr=[int(i) for i in file]
arr.sort()
sum=0
l=len(arr)
t=l//2
for i in range(t,l):
    sum+=arr[i]
print(sum)
##11877584