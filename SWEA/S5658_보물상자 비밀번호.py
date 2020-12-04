T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    password = list(input())
    password_set = set()
    turn = N//4
    for _ in range(turn):
        for i in range(4):
            password_set.add(''.join(password[i*turn:(i+1)*turn]))
        password.append(password.pop(0))
    # print(password_set)
    password_num = list()
    for num in password_set:
        password_num.append(int(num,16)) #10진수로 변경
    password_num.sort(reverse=True) # 내림차순

    print(f'#{tc} {password_num[K-1]}')
