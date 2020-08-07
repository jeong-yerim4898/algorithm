# 행렬 접근하기
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 2 3 2
# 0 0 3 2 1 3
# 0 0 2 1 3 4
# 0 0 0 0 0 0
# 위 행렬을 입력받아서
# 행렬에 포함되어 있는 sub matrix 크기 계산하기
T= int(input())
for test_case in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    mat_li=[]
    # 할일
    # matrix 순회하면서 0이 아닌 위치 찾기
    # 가로,세로 길이 구해서 저장
    # 표시한 영역은 0으로 다 바꾸기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                # 가로, 세로 길이 구하기
                x = 0  # 가로길이
                for k in range(j, N):
                    if matrix[i][k] != 0:
                        x += 1
                    else:
                        break
                # 세로길이
                y = 0
                for k in range(i, N):
                    if matrix[k][j]:
                        y += 1
                    else:
                        break
                # 표시한 영역은 0으로 다 바꾸기
                for k in range(i, i + y):
                    for l in range(j, j + x):
                        matrix[k][l] = 0
                mat_li.append((y,x,x*y))

    for i in range(len(mat_li) - 1):
        min = i
        for j in range(i + 1, len(mat_li)):
            if mat_li[min][2] > mat_li[j][2]:
                min = j
        mat_li[i], mat_li[min] = mat_li[min], mat_li[i]
    print(f'#{test_case} {len(mat_li)}',end=' ')
    for i in range(len(mat_li)):
        for k in range(2):
            print(f'{mat_li[i][k]}', end=' ')
    print()
