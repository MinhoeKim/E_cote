# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4

n = int(input())

m = int(input())

N, M = map(int, input().split())

array = [[0]*(N+1)]


for i in range(m):
    i, j, distance = map(int, input().split())

    if array[i][j] == 0:
        array[i][j] = distance
    elif distance < array[i][j]:
        array[i][j] = distance
print(array)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and array[i][k] != 0 and array[k][j] != 0:
                if array[i][j] == 0:
                    array[i][j] = array[i][k]+array[k][j]
                else:
                    array[i][j] = min(array[i][j], array[i][k]+array[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(array[i][j],end=' ')
    print()