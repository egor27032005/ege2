f = open('17 (4).txt', 'r')
numbers = [int(x) for x in f]
t=0
arr=[]
l=len(numbers)
for i in range(l-1):
    for j in range(i+1,l):
        if numbers[i]%160!=numbers[j]%160 and (numbers[i]%7==0 or numbers[j]%7==0):
            t+=1
            arr.append(numbers[i]+numbers[j])
arr.sort()
print(t)
print(arr[-1])
# 12749665 19989.