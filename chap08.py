# x = int(input())

# d = [0] * 30001

# for i in range(2, x + 1):

#     d[i] = d[i - 1] + 1

#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)

#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)

#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)

#     print(d[:31])

# print(d[x])

#==============================================================

# n = int(input())

# array = list(map(int, input().split()))

# d = [0] * 100

# d[0] = array[0]
# d[1] = max(array[0], array[1])
# for i in range(2, n):
#     d[i] = max(d[i - 1], d[i - 2] + array[i])
#     print(d[:5])

# print(d[n - 1])

#===================================================================

# n = int(input())

# d = [0] * 1001

# d[1] = 1
# d[2] = 3
# for i in range(3, n + 1):
#     d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796
    
    
# print(d[n])

#========================================================

n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    array_i = array[i]
    for j in range(array[i], m + 1):
        debug = d[j - array[i]]
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])