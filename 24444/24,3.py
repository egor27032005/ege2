file=open('14.txt', 'r')
s=file.readline().strip()
arr = [char for char in s]
l=len(arr)
st=''
for i in range(1,l):
    if arr[i]=="C":
        st+=arr[i]
    elif arr[i]!="C" and arr[i-1]=="C":
        st+=" "
all_lines=st.split()
print(len(max(all_lines, key=len)))
# print(len(max(all_lines, key=len)))