from itertools import combinations
from itertools import permutations

N = int(input())
mapping = [list(map(int,input().split())) for _ in range(N)]
ans= 9999999
for team in list(combinations(range(N),N//2)):
    s1=0
    s2=0
    s1_member = list()
    s2_member = list()
    c = [0] * N
    for t in team:
        c[t]=1
    for i in range(N):
        if c[i]==1:
            s1_member.append(i)
        else:
            s2_member.append(i)
    for one in list(permutations(s1_member,2)):
        s1+=mapping[one[0]][one[1]]
    for two in list(permutations(s2_member,2)):
        s2+= mapping[two[0]][two[1]]
    ans = min(ans,abs(s1-s2))
print(ans)

