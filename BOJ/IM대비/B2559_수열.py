
N,K = map(int,input().split()) # N 날짜수 , K 연속날짜수
nums = list(map(int,input().split()))

tmp = sum(nums[:K])
max_sum = tmp
for i in range(K,N):

    tmp += nums[i]
    tmp -= nums[i-K]
    if tmp>max_sum:
        max_sum= tmp


print(max_sum)