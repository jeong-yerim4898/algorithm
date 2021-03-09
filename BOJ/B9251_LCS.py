# s1=list(input())
# s2=list(input())
# dp=[0]*1001
# idx=-1
# for k in range(len(s1)):
#     cnt=0
#     for i in range(len(s1)):
#         for j in range(idx+1,len(s2)):
#             if s1[i]==s2[j]:
#                 cnt+=1
#                 idx=j
#                 break
#     dp[k]=cnt
# print(max(dp))

import sys
S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()
len1 = len(S1)
len2 = len(S2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
print(matrix[-1][-1])
