n, m = map(int, input().split())

balls = list(map(int, input().split()))


count = 0
for i in range(len(balls)-1):
    first = balls[i]
    for j in range(i+1, len(balls)):
        second = balls[j]
        if first != second:
            print(i+1, j+1)
            print('무게', first, second)
            print()
            count += 1

print(count)
