# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# result = 0
# for step in steps:
    
#     next_row = row + step[0]
#     next_column = column + step[1]

#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
#         result += 1
        
# print(result)

#===================================================================

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =  3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y  + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
        
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        
        else:
            break
        turn_time = 0
        
print(count)
