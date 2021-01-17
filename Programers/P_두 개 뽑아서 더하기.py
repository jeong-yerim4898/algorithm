from itertools import combinations

def solution(numbers):
    cases = list(combinations(numbers,2))
    ans=list()
    for case in cases:
        ans.append(sum(case))
    ans= sorted(list(set(ans)))
    return ans