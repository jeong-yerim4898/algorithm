from itertools import combinations

N,M= map(int,input().split())
cards = list(map(int,input().split()))
cases = [c for c in combinations(cards,3)]
max_ans = 0
for case in cases:
    if sum(case)<=M:
        if max_ans<=sum(case):
            max_ans=sum(case)
print(max_ans)