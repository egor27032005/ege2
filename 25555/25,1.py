for i in range(210235,210301):
    k=0
    a=[]
    for j in range(2,i//2+1):
        if i%j==0:
            k+=1
            a.append(j)
        if k>4:
            break
    if k==4:
        print(a)
# for i in range(150000, 200001,2):
#     n=2
#     t=0
#     c=0
#     while(n*n<i):
#         if i%n==0:
#             t+=1
#             c=n
#         n+=1
#     if t==48:
#         print(i,c)
# 