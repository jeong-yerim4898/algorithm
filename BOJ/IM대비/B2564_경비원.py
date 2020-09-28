# (0,0)에서의 거리
def check(dir,len):
    if dir == 1:
        return len
    elif dir ==2:
        return w+h+w-len
    elif dir ==3:
        return w+h+w+h-len
    elif dir==4:
        return w+len


w,h = map(int,input().split())

N = int(input())
shops=[list(map(int,input().split())) for _ in range(N)]

start_dir, start_dis = map(int,input().split())
# 동근 거리
stand = check(start_dir,start_dis)
ans = 0
for shop in shops:
    shop_dir, shop_dis = shop[0],shop[1]
    shop_check = check(shop_dir,shop_dis)
    ans +=min(2*(w+h)-abs(stand-shop_check),abs(stand-shop_check))
print(ans)

