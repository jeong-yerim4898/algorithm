'''
5
2 3 1 2 2
'''
N = int(input())
arr = list(map(int,input().split()))

arr.sort()
# cnt=0
# while N>0:
#     i=1
#     N-=arr[-1*i]
#     cnt+=1
#     i+=1
# print(cnt)
result=0 # 총 그룹의 수
cnt=0 # 현재 그룹에 포함된 모험가의 수
for i in arr:
    cnt+=1
    if cnt>=i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹결성
        result+=1
        cnt=0
print(result)
