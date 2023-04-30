file=open('58253_16134844255703_doc.txt', 'r')
s=file.readline().strip()
s=s.replace("A", " ")
s=s.replace("C", " ")

s=s.replace("A", " ")
s=s.replace("C", " ")


all_lines=s.split()
print(all_lines)
print(len(max(all_lines, key=len)))## Ответ 14
## Ответ 32