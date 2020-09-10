

T= int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split()) # 숫자 수 ,추가 칸수, 반복횟수
    original_li= list(map(int,input().split()))
    for _ in range(1):
        start = 0
        original_li[start+3:start+3]=original_li[start+2]+original_li[start+3]
        print(original_li)