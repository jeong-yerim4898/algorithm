from itertools import permutations

N = int(input())
num_li = list(map(int,input().split()))
case_li = list(permutations(num_li,N))
ans=-98765431
for num in case_li:
    tmp_ans = 0
    for i in range(1,N):
        tmp_ans+=abs(num[i-1]-num[i])
    if tmp_ans>ans:
        ans = tmp_ans
print(ans)