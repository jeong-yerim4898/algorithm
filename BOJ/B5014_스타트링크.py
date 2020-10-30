def solution(arr):
    def check(r, c, s):
        global one, zero
        sum_ele = 0

        for i in range(s):
            sum_ele += sum(arr[r+i][c:s])
        if s == 1:
            if arr[r][c] == 1:
                answer[1]+=1
                return
            else:
                answer[0]+=1
                return
        if sum_ele == 0:
            answer[0]+=1
            return
        elif sum_ele == s * s:
            answer[1]+=1
            return

        check(r, c, s // 2)
        check(r + s // 2, c, s // 2)
        check(r, c + s // 2, s // 2)
        check(r + s // 2, c + s // 2, s // 2)
        return
    answer = [0,0]
    N = int(len(arr))
    one = 0
    zero = 0
    check(0, 0, N)
    # answer.append(zero)
    # answer.append(one)
    print(answer)
    return answer

solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])