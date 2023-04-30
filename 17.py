# f = open('999.txt', 'r')
# numbers = [int(x) for x in f]
# sum=0
# t=0
# max=0
# for i in range(len(numbers)):
#     a=numbers[i]
#     k = 0
#     for i in range(2, a // 2+1):
#         if (a % i == 0):
#             k = k+1
#     if (k <= 0):
#         sum+=1
#         if a>max:
#             max=a
# print(max,sum)
sum=0
for i in range(124503, 124564):
    k=0
    for n in range(2, i // 2+1):
        if (i % n == 0):
             k = k+1
    if (k == 6):
         sum+=1
print(sum)
# Ответ 12