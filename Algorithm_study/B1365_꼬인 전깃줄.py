# def lis(arr):
#     dp[0]=1
#     for i in range(1,N):
#         maxval = 0
#         for j in reversed(range(i)):
#             if arr[j]<arr[i] and maxval<dp[j]:
#                 maxval=dp[j]
#         dp[i] = maxval+1
#     # print(dp)
#     return max(dp)

def lower_bound(start, end, target):
    while start < end:
        middle = (start + end) // 2
        if lis[middle] < target:
            start = middle + 1
        else:
            end = middle
    return end + 1


N = int(input())
power_li = list(map(int, input().split()))
lis = [0] * (N + 1)
plis = 0
parr = 1
cnt = 0
lis[plis] = power_li[0]
while parr < N:
    if lis[plis] < power_li[parr]:
        plis += 1
        lis[plis] = power_li[parr]
    else:
        ans = lower_bound(0, plis, power_li[parr])
        lis[ans - 1] = power_li[parr]
        cnt += 1

    parr += 1

print(cnt)
