N = int(input())
nums = list()
for _ in range(N):
    a,b = map(int,input().split())
    nums.append([a,b])
ans_li = sorted(nums,key =lambda x:(x[1],x[0]))
for ans in ans_li:
    print(ans[0],end=' ')
    print(ans[1])