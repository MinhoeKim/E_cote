from collections import deque

n = int(input())
k = int(input())
apples = []
board = [[0] * n for i in range(n)]

for i in range(k):
  x, y = map(int, input().split())
  apples.append((x-1, y-1))

for apple in apples:
  x, y = apple
  board[x][y] = 2

L = int(input())

X_C = []

east = (0,1)
west = (0,-1)
south = (1,0)
north = (-1,0)

direct_xy = [south,west,north]
direct_xy = deque(direct_xy)

for i in range(L):
  X, C = input().split()
  X = int(X)
  X_C.append((X, C))
X_C = deque(X_C)

time = 0
board[0][0] = 1
direct = east
x, y = 0, 0

loop = True
stop = 0
snake = [(0,0)]
snake = deque(snake)
while loop == True:
  
  if X_C:
    X, C = X_C.popleft()  
  
  
  while True:
    
    time += 1
    next_x = x + direct[0]
    next_y = y + direct[1]
    
    if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n:
      loop = False
      break

    if board[next_x][next_y] == 0:
      
      board[next_x][next_y] = 1
      a,b = snake.popleft()
      board[a][b] = 0
      snake.append((next_x,next_y))
      x = next_x
      y = next_y
    elif board[next_x][next_y] == 2:
      
      board[next_x][next_y] = 1
      snake.append((next_x,next_y))
      x = next_x
      y = next_y
    elif board[next_x][next_y] == 1:
      loop = False
      break
    
    if time == X:
      if C == 'D':
        direct_xy.append(direct)
        direct = direct_xy.popleft()
        break
      if C == 'L':
        direct_xy.appendleft(direct)
        direct = direct_xy.pop()
        break
    
  
print(time)

