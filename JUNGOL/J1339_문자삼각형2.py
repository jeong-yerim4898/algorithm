n = int(input())
alpabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mapping=[[0]*n for _ in range(n)]
idx=0
tmp=-1
if 0<n<101 and n%2!=0:
    for c in range(n // 2, -1, -1):
        tmp += 1
        for r in range(n // 2 - tmp, n // 2 + tmp + 1):
            mapping[r][c] = alpabet[idx % 26]
            idx += 1

    for r in range(n):
        for c in range(n):
            if mapping[r][c] != 0:
                print(mapping[r][c], end=' ')
            else:
                print(' ', end=' ')
        print()
else:
    print('INPUT ERROR')
