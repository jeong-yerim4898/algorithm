'''
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''
ans=-987654
N,M = map(int,input().split()) # 행,열
for n in range(N):
    arr = list(map(int,input().split()))
    # 받은 배열의 제일 최소값 찾기
    min_val = min(arr)
    if ans<min_val:
        ans=min_val
print(ans)