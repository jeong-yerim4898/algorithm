
N = int(input()) # 스위치 갯수
switch_li = list(map(int,input().split()))
M = int(input())

for i in range(M):
    sex, num = map(int,input().split())
    if sex==1:
        for j in range(num-1,len(switch_li),num):
            switch_li[j]=switch_li[j]^1
    else:
         #인덱스 통일
        num-=1
        switch_li[num]=switch_li[num]^1
        for j in range(1,min(len(switch_li)-num,num+1)):
            if switch_li[num-j]==switch_li[num+j]:
                switch_li[num-j]=switch_li[num-j]^1
                switch_li[num+j]=switch_li[num+j]^1
            else:
                break
print(switch_li[0],end=' ')
for i in range(1,len(switch_li)):
    if(i)%20==0:
        print()
    print(switch_li[i],end=' ')