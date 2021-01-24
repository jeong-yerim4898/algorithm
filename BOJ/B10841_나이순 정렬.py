N= int(input())
people=list()
for _ in range(N):
    age,name= map(str,input().split())
    people.append([int(age),name])
ans_li = sorted(people,key=lambda x:x[0])
for ans in ans_li:
    print(ans[0],end=' ')
    print(ans[1])