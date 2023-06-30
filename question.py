# INF = int(1e9)

# N = int(input())

# house = list(map(int, input().split()))

# min_num = min(house)
# max_num = max(house)


# min_sum = INF
# point = 0
# for i in range(min_num,max_num+1):
#     length = 0
#     for j in house:
#         length += abs(i-j)
#     if length < min_sum:
#         min_sum = length
#         point = i
        
# print(point)


n = int(input())
data = list(map(int, input().split()))
data.sort()

print(3/2)
print(data[(n-1)//2])
    