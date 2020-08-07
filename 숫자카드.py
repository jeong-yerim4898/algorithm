T = int(input())
for test_case in range(1, T + 1):
    cards = int(input())
    num = list(map(int, input()))
    cnt_li = [0]*10
    cnt_value = 0
    for j in num:
        cnt_li[j] += 1
    for i in range(len(cnt_li)):
        if cnt_li[i] >= cnt_value:
            cnt_value = cnt_li[i]
            number = i

    print(f'#{test_case} {number} {cnt_value}')