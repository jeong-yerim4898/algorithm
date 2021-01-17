def solution(arr):
    def check(r, c, s):
        standard = arr[r][c]
        for i in range(r, r + s):
            for j in range(c, c + s):
                if arr[i][j] != standard:
                    check(r, c, s // 2)
                    check(r + s // 2, c, s // 2)
                    check(r, c + s // 2, s // 2)
                    check(r + s // 2, c + s // 2, s // 2)
                    return
        tmp.append(standard)

    answer = []
    tmp = []
    N = int(len(arr))
    check(0, 0, N)
    one = 0
    zero = 0
    for ele in tmp:
        if ele == 1:
            one += 1
        else:
            zero += 1
    answer.append(zero)
    answer.append(one)
    return answer

