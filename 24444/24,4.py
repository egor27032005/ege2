file=open('14.txt', 'r')
s=file.readline().strip()
s=s.replace("A", " A ")
s=s.replace("E", " E ")
all_lines=s.split()
l=len(all_lines)

print(len(max(all_lines, key=len)))