N = int(input())
N_li = list(int(input()) for _ in range(N))
for i in sorted(N_li):
    print(i)