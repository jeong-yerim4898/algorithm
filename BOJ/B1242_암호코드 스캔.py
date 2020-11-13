import sys
sys.stdin=open('sample_input.txt')


hex = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101',
       '6':'0110','7':'0111','8':'1000','9':'1001',
       'A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
code_pattern = {'112':0,'122':1,'221':2,'114':3,'231':4,'132':5,'411':6,'213':7,'312':8,'211':9}

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #N세로 M가로
    board = [list(input()) for _ in range(N)]
    # print(board)

# 16진수 -> 2진수
    bi_li = ['']*N
    for i in range(N):
        for j in range(M):
            bi_li[i] += hex[board[i][j]]
    # print(bi_li)
    result = []
    visitied = []
    ans = 0

# 2진수 -> 암호 코드
    for y in range(N):
        c1 =c2 =c3 = 0
        for k in range((M*4)-1,-1,-1): #16진수가 2진수로 늘어났기 때문에 *4
            if c2 == 0 and c3 ==0 and bi_li[y][k]=='1': # 첫번째 만나는 pattern '1'
                c1+=1
            elif c1>0 and c3 == 0 and bi_li[y][k]=='0': # 두번째 만나는 pattern '0'
                c2+=1
            elif c1>0 and c2>0 and bi_li[y][k]=='1': #세번쨰로 만난느 pattenr '1'
                c3+=1
            if c1>0 and c2>0 and c3>0 and bi_li[y][k]=='0':
                min_check = min(c1,c2,c3)
                c1 = c1//min_check
                c2 = c2//min_check
                c3 = c3//min_check
                pattern = code_pattern[str(c1)+str(c2)+str(c3)]
                result.append(pattern)
                c1 =c2 =c3 =0
# 암호코드 검증
            if len(result)==8:
                result2 = result[::-1]
                value = ((result2[0]+result2[2]+result2[4]+result2[6])*3)+(result2[1]+result2[3]+result2[5])+result2[7]
                if value%10==0 and result2 not in visitied:
                    ans+=sum(result)
                visitied.append(result2)
                result = []
    print(f'#{tc} {ans}')

