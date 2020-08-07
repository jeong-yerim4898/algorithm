T = int(input())
for test_case in range(1, T + 1):
    info = list(map(int, input().split()))

    result = []
    for j in range(2):
        start = 1
        end = info[0]
        page = info[j + 1]
        cnt = 0

        while start <= end:
            mid = (start + end) // 2
            if mid == page:
                break
            elif mid < page:
                start = mid
                cnt += 1
            else:
                end = mid
                cnt += 1
        result.append(cnt)

    if result[0] == result[1]:
        print(f'#{test_case} 0')
    elif result[0] < result[1]:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} B')