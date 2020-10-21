
T = int(input())
for tc in range(1,T+1):
    t = int(input())
    score = [0]*101
    ans = 0
    idx = 0
    arr = list(map(int,input().split()))
    for i in arr:
        score[i]+=1
    for j in range(1,101):
        if ans<=score[j]:
            ans = score[j]
            idx = j
    print(f'#{tc} {idx}')