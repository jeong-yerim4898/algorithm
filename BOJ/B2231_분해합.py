N = int(input())
ans =0
for num in range(1,N+1):
    num_li = list(map(int,str(num)))
    if num+sum(num_li) == N:
        print(num)
        break
    if num==N:
        print(0)