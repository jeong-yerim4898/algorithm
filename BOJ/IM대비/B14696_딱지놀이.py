
N = int(input())

for _ in range(N):
    a_cnt = [0]*5
    b_cnt = [0]*5
    a= list(map(int,input().split()))
    for i in range(a[0]):
        a_cnt[a[i+1]]+=1
    b = list(map(int,input().split()))
    for i in range(b[0]):
        b_cnt[b[i+1]]+=1
    if a_cnt[4]!=b_cnt[4]:
       if a_cnt[4]>b_cnt[4]:
           print('A')
       else:
           print('B')
    elif a_cnt[3]!=b_cnt[3]:
        if a_cnt[3] > b_cnt[3]:
            print('A')
        else:
            print('B')
    elif a_cnt[2]!=b_cnt[2]:
        if a_cnt[2] > b_cnt[2]:
            print('A')
        else:
            print('B')
    elif a_cnt[1]!=b_cnt[1]:
        if a_cnt[1] > b_cnt[1]:
            print('A')
        else:
            print('B')
    else:
        print('D')
