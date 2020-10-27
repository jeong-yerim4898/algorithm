def find_code(scanner):
    global N,M,data
    for r in range(N):
        for c in range(M-1,-1,-1): # 제일 뒤가 무조건 1이기 때문에 뒤부터 찾기
            if scanner[r][c]=='1':
                data = scanner[r][c-55:c+1]
                return data

code_dic = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,
            '0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    scanner = [input() for _ in range(N)]
    data =str()
    find_code(scanner)

    ans = list()
    start_idx = 0
    end_idx = 6
    for _ in range(8):
        ans.append(code_dic[data[start_idx:end_idx+1]])
        start_idx+=7
        end_idx+=7
        # print(ans)
    calculate = ((ans[0]+ans[2]+ans[4]+ans[6])*3)+(ans[1]+ans[3]+ans[5])+ans[7]

    if not calculate%10:
        print(f'#{tc} {sum(ans)}')
    else:
        print(f'#{tc} 0')