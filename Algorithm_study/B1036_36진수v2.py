'''
5
GOOD
LUCK
AND
HAVE
FUN
7
'''
def threesix_to_decimal(c):
  num = ord(c)
  if 48 <= num <= 57:  # num은 숫자이다.
    return num - 48
  elif 65 <= num <= 90:
    return num - 65 + 10  # 16진법으로 10이상 하기 때문

def decimal_to_36(n):
  S = ''
  if n == 0:
    S='0'
  else:
    while n>0:
      a,b =divmod(n,36)
      if 0<=b<=9:
        S+=chr(b+48)
      else:
        S+= chr(b+55)
      n=a
  return S

K = int(input())
value = [0]*36
for _ in range(K):
  numbers = input()
  for j in range(len(numbers)):
    real_num = threesix_to_decimal(numbers[j])
    value[real_num]+=36**(len(numbers)-j-1) # 36승에 대한 해당 숫자별 누적 값
# print(value)
K = int(input())
multi = [[value[i]*(35-i),i] for i in range(36)] #Z와 차이가 가장 큰것
multi.sort() # 2차원 배열일 때 idx 0을 기준으로 오름차순으로 배열이 된다.
ans = 0
for i in range(36-K):
  ans += multi[i][1]*value[multi[i][1]]
for j in range(36-K,36): # K만큼 Z로 바꾸기
  ans += 35 * value[multi[j][1]]
# print(ans)
print(decimal_to_36(ans)[::-1])