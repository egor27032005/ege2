f = open('17 (3).txt', 'r')
numbers = [int(x) for x in f]
l=len(numbers)
arr=[]
sum=0
t=0
for i in range(l-1):
    sum=0
    if numbers[i]%3==0 or numbers[i+1]%3==0:
        t+=1
        sum=numbers[i+1]+numbers[i]
        arr.append(sum)
arr.sort()
print(t)
print(arr[-1])