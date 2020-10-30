

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 신청서 숫자
    papers =[list(map(int,input().split())) for _ in range(N)]
    papers2 = sorted(papers,key = lambda x: x[1])
    # print(papers2)
    result=0
    recent = 0
    while papers2:
        start , end = papers2.pop(0)
        if start>=recent:
            result+=1
            recent= end
    print(f'#{tc} {result}')