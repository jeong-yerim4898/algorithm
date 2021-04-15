'''
25 5
'''
N,K = map(int,input().split())
cnt=0
while N>1:
    # 나ㅝ 떨어진다면
    if N%K==0:
        N = N//K
        cnt+=1
    else:
        N-=1
        cnt+=1
print(cnt)