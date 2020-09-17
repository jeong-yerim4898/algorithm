
N = int(input()) # 한변의 길이
K = int(input()) # 제거 타일의 개수
# remove_tile = [list(map(int,input().split())) for _ in range(K)] # 1빨간 2파란 3노란
half = N//2
while K>0:
    K-=1
    ele = list(map(int,input().split()))
    if ele[1]<=half:
        start = ele[1]
        end = N+1-ele[1]
        if (start<=ele[0]<=end):
            color = ele[1]%3
        else:
            if ele[0]<=half:
                color = ele[0]%3
            else:
                color = (N+1-ele[0])%3

    else:
        start = N+1-ele[1]
        end = ele[1]
        if (start<=ele[0]<=end):
            color = (N+1-ele[1])%3
        else:
            if ele[0]<=half:
                color = ele[0]%3
            else:
                color = (N+1-ele[0])%3


    if color ==0:
        color = 3
    print(color)

