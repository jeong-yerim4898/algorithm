def solution(s):
    answer = 98765431
    result = ''
    if len(s) == 1:
        return 1
    for k in range(1, len(s) // 2 + 1):
        st = s[:k]
        cnt = 1
        for i in range(k, len(s), k):
            if s[i:i + k] == st:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                result += str(cnt) + st
                st = s[i:i + k]
                cnt = 1
        if cnt == 1:
            cnt = ''
        result += str(cnt) + st
        if answer > len(result):
            answer = len(result)
        result = ''
    return answer
solution('aabbaccc')