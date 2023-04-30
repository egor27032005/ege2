f = open('11111.txt', 'r')
n = int(f.readline().strip())
# numbers = [int(x.strip()) for x in f]
# count = 0
# for i in range(n - 4):
#     for j in range(i + 4, n):
#         if numbers[i] % 29 == 0 or numbers[j] % 29 == 0:
#             count += 1
# print(count)
# 3262771
n_54 = 0
queue = [int(f.readline().strip()) for i in range(7)]
count = 0
for i in range(0, 7):
    if queue.pop(0) % 54 == 0:
        n_54 += 1
    queue.append(int(f.readline().strip()))
    if queue[-1] % 54 == 0:
        count += i - 4 + 1
    else:
        count += n_54
print(queue)