# file = open('qqqq.txt')
# N = int(file.readline())
# arr = []
# sum=0
# for i in range(N):
#     x = int(file.readline())
#     for y in arr:
#         if x * y % 14 == 0:
#             sum+=1
#     if len(arr) >= 3:
#         arr.pop(0)
#     arr.append(x)
# print(sum)
#Ответ 54239
f = open('27_2018_C.txt', 'r')
n = int(f.readline().strip())
k = 0
k2 = 0
k13 = 0
k26 = 0
k_all = 0
for i in range(n):
    x = int(f.readline())
    if x % 26 == 0:
        k += k_all
    elif x % 13 == 0:
        k += k2
    elif x % 2 == 0:
        k += k13
    else:
        k += k26
    k_all += 1
    if x % 2 == 0:
        k2 += 1
    if x % 13 == 0:
        k13 += 1
    if x % 26 == 0:
        k26 += 1
print(k)