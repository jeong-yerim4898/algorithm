import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    pw_li = list(input())[:-1]
    left,right = [],[]
    for pw in pw_li:
        if pw=='<':
            # 왼쪽 배열에 문자가 남아있다면
            if left:
                right.append(left.pop())
        elif pw=='>':
            if right:
                left.append(right.pop())
        elif pw=='-':
            if left:
                left.pop()
        else:
            left.append(pw)
    print(''.join(left)+''.join(right[::-1]))