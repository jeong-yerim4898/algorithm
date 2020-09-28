
n = int(input())
number = list(map(int,input().split()))

ans = list()
for i in range(len(number)):
    if i ==0: # 제일 처음 도착하는 친구
        ans.append(i+1)
    else:
        change = number[i]
        if change==0:
            ans.append(i+1)
        else: # 제자리 아닌경우
            ans.insert(i-change,i+1)

print(*ans,end=' ')
