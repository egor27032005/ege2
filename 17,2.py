f = open('58165_16341465327506_doc.txt', 'r')
numbers = [int(x) for x in f]
s=len(numbers)
v=0
sum=0
for i in range(s):
    if numbers[i]%29==0 and numbers[i]%13!=0 and numbers[i]%17!=0 and numbers[i]%31!=0:
        v+=1
        sum+=numbers[i]
        print(numbers[i])
print(v)
print(sum)