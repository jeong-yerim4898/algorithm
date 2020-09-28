#1동 2서 3남 4북
# 넓이 최대 - 작은 사각형
N = int(input())
ground = [list(map(int,input().split())) for _ in range(6)]
big=0
k=0
for i in range(6):
    if big<(ground[i][1]*ground[(i+1)%6][1]):
        big = ground[i][1]*ground[(i+1)%6][1]
        k=i
# 작은 사각형
small = (ground[(k+3)%6][1]*ground[(k+4)%6][1])
ans = (big-small)*N
print(ans)