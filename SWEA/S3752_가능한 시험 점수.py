T = int(input())
for tc in range(1,T+1):
    N = int(input()) # qnswptn
    scores = list(map(int,input().split()))
    score_case = [0]*(sum(scores)+1)
    score_case[0]=1

    for score in scores:
        for i in range(sum(scores),-1,-1):
            if score_case[i]:
                score_case[i+score]=1
    print(f'#{tc} {score_case.count(1)}')