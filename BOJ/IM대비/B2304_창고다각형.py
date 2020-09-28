
N =int(input())

build_li = [list(map(int,input().split())) for _ in range(N)]
build_li.sort()
new_build = [0]*(build_li[-1][0]+1)
for li in build_li:
    i=li[0]
    new_build[i]=li[1]

max_idx = new_build.index(max(new_build))

height = 0
for i in range(max_idx):
    if height<new_build[i]:
        height = new_build[i]
    else:
        new_build[i]=height


height=0
for j in range(len(new_build)-1,max_idx,-1):
    if height<new_build[j]:
        height = new_build[j]
    else:
        new_build[j]=height
print(sum(new_build))

