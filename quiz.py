n = int(input())

array = []
temp = [[0] * n for _ in range(n)]


for _ in range(n):
    array.append(list(input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

student = 3
result = 'no'


def go_straight(i, x, y):
    global student
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
        if temp[nx][ny] == 'X':
            temp[nx][ny] = 'V'
            go_straight(i, nx, ny)

        # if temp[nx][ny] == 'O':

        if temp[nx][ny] == 'S':
            student -= 1
            temp[nx][ny] = 'V'
            go_straight(i, nx, ny)


def view(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if array[nx][ny] == 'X' or array[nx][ny] =='S':
                temp[nx][ny] = 'V'
                go_straight(i, nx, ny)


debug = 0


def dfs(count):
    global student
    global result
    global debug

    if count == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = array[i][j]

        for i in range(n):
            for j in range(n):
                if temp[i][j] == 'T':
                    view(i, j)
                    
        if debug == 1:
            print()
            print()
            
            
        print(student)
        if student == 3:
            print('yes')
            result = 'yes'
            
        else:
            student = 3
        #   print('no')
            
        return
    for i in range(n):

        for j in range(n):
            if array[i][j] == 'X':
                array[i][j] = 'O'
                count += 1
                
                if count == 1 and i == 0 and j == 3:
                    debug = 1

                dfs(count)

                array[i][j] = 'X'
                count -= 1


dfs(0)
print(result)
