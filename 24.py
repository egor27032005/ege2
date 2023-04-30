file=open('17 (5).txt', 'r')
s=file.readline().strip()
s=s.replace("B", " ")
s=s.replace("A", " ")

all_lines=s.split()
print(all_lines)
print(len(max(all_lines, key=len)))
##Ответ 32
# g=0
# l=len(all_lines)
# for i in range(l):
#     if all_lines[i].count("F")>0 and len(all_lines[i])<16 and all_lines[i][0]=="A" and all_lines[i][-1]=="B":
#         print(all_lines[i])
#         g+=1
# print(g)
##print(max(all_lines, key=len))
##print(len(max(all_lines, key=len)))## Ответ 14
## Ответ 32