

T = int(input()) # testcase
for tc in range(1,T+1):
    N = int(input()) # N일
    price = list(map(int,input().split()))[::-1] # 처음에 하고 후에 높은 가격에 팔기 때문에 뒤에서 부터 시작한다.
    ans = 0 # 최종 답
    now_max = price[0] # 현 시점 최고 가격 (적어도 제일 뒤에서 물건을 팔기 때문에)

    for i in range(1,N): # 현 시점 다음부터 비교하기 위해
        if now_max>price[i]: # 현시점 가격이 크다면
            ans += now_max-price[i] # now_max가 사는 가격이 되고 pirce는 파는 가격이기 때문에 차만큼 더해준다.
        else:
            now_max = price[i]

    print(f'#{tc} {ans}')