def merge_sort(li):
    if len(li)<=1:
        return li
    mid = len(li)//2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])

    i,j,k=0,0,0
    # 분할 된 부분 끼리 비교
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            li[k]=left[i]
            i+=1
        else:
            li[k]=right[j]
            j+=1
        k+=1
    # 한 쪽이 먼저 끝난 경우
    if i==len(left):
        while j<len(right):
            li[k]=right[j]
            j+=1
            k+=1
    elif j==len(right):
        while i<len(left):
            li[k]=left[i]
            i+=1
            k+=1
    return li

N = int(input())
N_li = list(int(input()) for _ in range(N))
num = merge_sort(N_li)

for i in num:
    print(i)