T = int(input())
for test_case in range(1, T + 1):
    turn = int(input())
    nums = list(map(int,input().split()))
    max_num = 0
    min_num = 1000000000000
    for i in nums:
        if i>max_num:
            max_num =i
    for j in nums:
        if j<min_num:
            min_num = j
    print(f'# {test_case} {max_num-min_num}')