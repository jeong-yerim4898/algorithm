# N = int(input())
# N_li = list(int(input()) for _ in range(N))
# for i in range(N-1):
#     for j in range(N-1-i):
#         if N_li[j]>N_li[j+1]:
#             N_li[j],N_li[j+1]=N_li[j+1],N_li[j]
# for i in sorted(N_li):
#     print(i)