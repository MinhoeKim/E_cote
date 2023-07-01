n = int(input())
tower = []
for i in range(n):
    tower.append(list(map(int, input().split())))

temp = [[]]

for i in range(n-1):
    temp.append(tower[i])


for i in range(n-1, 0, -1):
    for j in range(len(tower[i])-1):
        if tower[i][j] > tower[i][j+1]:
            temp[i][j] = tower[i][j]+temp[i][j]
        else:
            temp[i][j] = tower[i][j+1]+temp[i][j]


print(*temp[1])
