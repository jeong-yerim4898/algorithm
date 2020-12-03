from itertools import combinations

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    mapping=[list(map(int,input().split())) for _ in range(N)]
    food = [i for i in range(N)]
    material_li = [k for k in combinations(food,N//2)]
    ans = 9874654321
    for idx in range(len(material_li)//2):
        a_li = list(material_li[idx])
        b_li= list(material_li[len(material_li)-idx-1])
        # print(a_li,b_li)
        sum_a,sum_b = 0,0
        for a in combinations(a_li,2):
            sum_a+=mapping[a[0]][a[1]]+mapping[a[1]][a[0]]
            # print(sum_a)
        for b in combinations(b_li,2):
            sum_b+=mapping[b[0]][b[1]]+mapping[b[1]][b[0]]
            # print(sum_b)
        if ans>abs(sum_a-sum_b):
            ans = abs(sum_a-sum_b)
            # print(ans)
    print(f'#{tc} {ans}')