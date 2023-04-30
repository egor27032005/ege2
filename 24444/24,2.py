file=open('1111.txt', 'r')
arr=file.readline().strip()
l=len(arr)
a1="BCD"
a2="BDE"
a3="BCE"
p=0
st=''
s = [char for char in arr]
for i in range(l-2):
    st=s[i]+s[i+1]+s[i+2]
    if s[i] in a1 and s[i+1] in a2 and s[i+2] in a3 and s[i]!=s[i+1] and s[i+1]!=s[i+2] and st!="CBC":
        p+=1
        print(p,s[i]+s[i+1]+s[i+2])
print()
