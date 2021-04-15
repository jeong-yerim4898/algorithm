'''
5 8 3
2 4 5 4 6
'''
# 46
N,M,K = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort() # 배열 정렬
num1 = arr[-1] # 제일 큰 값
num2 = arr[-2] # 두번 째로 큰 값
ans=0
while True:
    for i in range(K):
        if M==0:
            break
        ans+=num1
        M-=1
    if M==0:
        break
    ans+=num2
    M-=1
print(ans)