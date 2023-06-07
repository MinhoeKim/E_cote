import time

int(input())
fear = list(map(int, input().split()))

start_time = time.time()

# print(fear)

fear.sort()
group = 0

while len(fear) != 0:

    max = fear[-1]

    for i in range(max):
        if len(fear) == 0:
            break
        fear.pop()

    group += 1
    # end_time = time.time()
    # print("time :", end_time - start_time)


print(group)
end_time = time.time()
print("time :", end_time - start_time)


# n = int(input())
# data = list(map(int, input().split()))

# start_time = time.time()

# data.sort()

# result = 0
# count = 0

# for i in data:
#     count += 1
#     if count >= i:
#         result += 1
#         count = 0

# print(result)
# end_time = time.time()
# print("time :", end_time - start_time)

# start_time = time.time()
# for i in range(10):
#     for j in range(10):
#         print(j)
        
# end_time = time.time()
# print("time :", end_time - start_time)