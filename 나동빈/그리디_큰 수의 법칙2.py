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

# 큰 수가 더해지는 갯수 구하기
cnt = int(M//(K+1))*K
cnt+= M%(K+1)

ans=0
ans+=cnt*num1
ans+=(M-cnt)*num2
print(ans)