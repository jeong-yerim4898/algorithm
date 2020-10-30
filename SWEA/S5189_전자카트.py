# 순열
# dfs

def dfs(idx):
    global min_value,result
    if min_value>result:
        visited[idx]=True

        if False not in visited: # 다 방문 했다면
            result += mapping[idx][0]
            if min_value>result:
                min_value=result
            result-=mapping[idx][0]
        else:
            for next_idx in range(N):
                if not visited[next_idx]:
                    result += mapping[idx][next_idx]
                    dfs(next_idx)
                    result -= mapping[idx][next_idx]
        visited[idx]=False


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mapping = [list(map(int,input().split())) for _ in range(N)] #0번 사무실
    # print(mapping)
    min_value = 987654321
    result = 0
    visited = [False] * N
    dfs(0) #start, end

    print(f'#{tc} {min_value}')
