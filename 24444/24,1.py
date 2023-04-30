file=open('11111.txt', 'r')
s=file.readline().strip()
# s=s.replace("E", " ")
# s=s.replace("A", " ")
# s=s.replace("E", " ")
# s=s.replace("A", " ")
# all_lines=s.split()
arr = [char for char in s]
res=[]
l=len(arr)
t="0123456789"
f="QWERTYUIOPASDFGHJKLMNBVCXZ"
for i in range(1,l):
    if arr[i] in t:
        res.append(arr[i])
    elif arr[i] in f and arr[i-1] in t:
        res.append(" ")
st=''.join(res)
all_lines=st.split(" ")
print(all_lines)
l=len(all_lines)-1
k=0
for i in range(l):
    s=str(all_lines[i])
    if int(s[0])+int(s[1])==int(s[-1])+int(s[-2]):
        k+=1
        print(k,s)

# print(len(max(all_lines, key=len)))
# A, B, C, D, E, F. Найдите длину самой длинной подцепочки, не содержащей гласных букв.
# li = list(s)
# li[5] = 'A'
# result = ''.join(li)
