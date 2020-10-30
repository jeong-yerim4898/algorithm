#[+,-,*,/] operator
#dfs?
'''
1
5
2 1 0 1
3 5 3 7 9
'''

def dfs(idx,result):
    global min_result,max_result,next_result
    if idx==N-1: #연산자의 갯수는 주어진 숫자의 갯수보다 하나 작다.
        if min_result>=result:
            min_result = result
        if max_result<=result:
            max_result=result
        return
    for i in range(4):
        if operator[i]>0: # 연산자가 존재할 때
            operator[i]-=1 #연산자를 하나 사용한다.
            if i==0: #더하기 인 경우
                next_result = result+nums[idx+1]
            elif i==1:
                next_result = result-nums[idx+1]
            elif i==2:
                next_result = result*nums[idx+1]
            else:
                next_result = int(result/nums[idx+1])
            dfs(idx+1,next_result)
            operator[i]+=1
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    operator  = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    min_result = 987654321
    max_result = -78945612 # 마이너스도 나올수 있기때문에 0이면 안된다.
    next_result = 0
    dfs(0,nums[0])#idx, result 누적으로 가져다주기
    # print(max_result)
    # print(min_result)
    print(f'#{tc} {max_result-min_result}')