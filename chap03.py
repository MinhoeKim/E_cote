# n, m, k = map(int, input().split())

# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

# print(result)

# =================================
# n, m, k = map(int, input().split())

# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# count = int(m / (k + 1)) * k
# count += m % (k + 1)

# result = 0
# result += count * first
# result += (m - count) * second

# print(result)

# ==========================================

# n, m = map(int, input().split())

# result = 0

# for i in range(n):
#     data = list(map(int, input().split()))

#     min_value = min(data)

#     result = max(result, min_value)

# print(result)

# ===========================================

# n, k = map(int, input().split())
# result = 0

# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1

#     n //= k
#     result += 1

# while n > 1:
#     n -= 1
#     result += 1

# print(result)

# =======================================
n, k = map(int, input().split())
result = 0

while True:

    target = (n//k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    n //= k
    result += 1

result += (n-1)
print(result)
