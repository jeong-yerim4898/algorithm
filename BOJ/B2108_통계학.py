import sys
from collections import Counter
def san(li):
    return round(sum(li)/N)
def medium(li):
    tmp = sorted(li)
    return tmp[N//2]
def mode(li):
    tmp = Counter(li)
    tmp = sorted(tmp.items(), key=lambda x:(-x[1],x[0]))
    return tmp[1][0] if tmp[0][1]==tmp[1][1] else tmp[0][0]
def num_range(li):
    return max(li)-min(li)
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
print(san(nums))
if N==1:
    print(nums[0])
    print(nums[0])
    print(0)
    sys.exit()
print(medium(nums))
print(mode(nums))
print(num_range(nums))