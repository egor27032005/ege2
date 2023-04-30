file = open('uuuu.txt')
N = int(file.readline())
max_58=0
max_ob=0







max_2=0 
arr = [int(x) for x in file]
for i in range(N):
    if arr[i]%29==0:
        max_29=max(max_29,arr[i])
    if arr[i]%2==0:
        max_2=max(max_2,arr[i])
    if arr[i]%58==0:
        max_58=max(max_58,arr[i])
    max_ob=max(max_ob,arr[i])
max1=2
max2=1
if max_29!=max_2:
    max1=max_29*max_2
if max_58!=max_ob:
    max2=max_58*max_ob
print(max(max1,max2))
# А:44633204
# В:99760000