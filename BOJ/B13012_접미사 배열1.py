# 문제이해 실패
def solve(s):
    l = len(s)
    suffix_arr = sorted(range(len(s)),key=lambda i:s[i:])
    rank = [0]*l

    for k in range(l):
        rank[suffix_arr[k]]=k
    if s[suffix_arr[0]]>'a':
        return 1

    for k in range(1,l):
        pre = suffix_arr[k-1]
        i = suffix_arr[k]

        if ord(s[i])-1 > ord(s[pre]): # 바꾼게 전 꺼보다 크다면 순서가 맞다.
            return 1
        if ord(s[i])-1 == ord(s[pre]): #바꾼게 전이랑 같다면
            if i+1<l and pre+1 <l and rank[pre+1]<rank[i+1]: # 전체 길이보다 안에 있고 전 값이 바꾼 값보다 작다면
                return 1
            elif i+1<l and pre+1>=l:
                return 1
    return 0

if __name__=='__main__':
    s = input().strip()
    ans = solve(s)
    print(ans)