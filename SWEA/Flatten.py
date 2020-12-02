def max_num(li):
    maxx = 0
    for a in li:
        if a > maxx:
            maxx = a
    return maxx


def min_num(li):
    minn = 10000000000
    for a in li:
        if a < minn:
            minn = a
    return minn


for test_case in range(1,2):
    turn = int(input())
    build_li = list(map(int, input().split()))

    for turn_n in range(turn):
        build_li[build_li.index(max_num(build_li))] = max_num(build_li) - 1
        build_li[build_li.index(min_num(build_li))] = min_num(build_li) + 1
print(f'#{test_case} {max_num(build_li) - min_num(build_li)}')


