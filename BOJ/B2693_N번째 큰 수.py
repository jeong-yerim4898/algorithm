# 삽입정렬
def insert_sort(li):
    for i in range(1,len(li)):#1번 idx부터 설정하기
        j=i
        while j>0 and li[j-1]>li[j]: #만약 기준보다 전 값이 크다면
            li[j-1],li[j]= li[j],li[j-1]
            j-=1
    return li
T = int(input())
for tc in range(1,T+1):
    li = list(map(int,input().split()))
    insert_sort(li) #오름차순 정렬
    print(li[-3])