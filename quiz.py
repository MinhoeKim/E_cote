
```python
n = int(input())

num = [int(x) for x in str(n)]

half = int(len(num)/2)

if sum(num[:half]) == sum(num[half:]):
    print("LUCKY")
else:
    print("READY")
```

```python
string = input()

number = [int(i) for i in string if ord(i)<58 ]

abc = [i for i in string if ord(i)>58]

abc.sort()
number = sum(number)

for i in abc:
  print(i,end='')
print(number)
```

```python
s = input()

answer = len(s)

for i in range(1,len(s)):
    str_temp = s[0:i]
    count = 1
    compressed = ''
    for j in range(i, len(s), i):
        # if j+i >= len(s):
        #     compressed += str(count) + str_temp if count >= 2 else str_temp
        #     break
        
        if str_temp == s[j:j+i]:
            
            count += 1

        else: 
            compressed += str(count) + str_temp if count >= 2 else str_temp
            str_temp = s[j:j+i]
            count = 1
				
        if j+i >= len(s):
            compressed += str(count) + str_temp if count >= 2 else str_temp
            break

    # print(compressed)        
    answer = min(answer,len(compressed))

print(answer)
```

```python
def rotate_a_matrix_by_90_degree(a):
  n = len(a)
  m = len(a[0])
  result = [[0]*n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

def check(new_lock):
  lock_length = len(new_lock) // 3
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length,lock_length * 2):
      if new_lock[i][j] != 1:
        return False
  return True

m, n = map(int, input().split())

key = []
lock = []

for i in range(m):
  key.append(list(map(int,input().split())))

for i in range(n):
  lock.append(list(map(int, input().split())))

new_lock = [[0]*(n*3) for _ in range(n*3)]

for i in range(n):
  for j in range(n):
    new_lock[i + n][j + n] = lock[i][j]

for rotation in range(4):
  key = rotate_a_matrix_by_90_degree(key)
  for x in range(n*2):
    for y in range(n*2):
      for i in range(m):
        for j in range(m):
          new_lock[x+i][y+j] += key[i][j]
      if check(new_lock)== True:
          print(True)
          exit(0)
      for i in range(m):
        for j in range(m):
          new_lock[x+i][y+j] -= key[i][j]
print(False)
```

```python
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
```

```python
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        elif stuff == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
#     1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
n = 5
answer = []

for frame in build_frame:
    x, y,  stuff, operate = frame
    if operate == 0:
        answer.remove([x, y, stuff])
        if not possible(answer):
            answer.append([x, y, stuff])
    if operate == 1:
        answer.append([x, y, stuff])
        if not possible(answer):
            answer.remove([x, y, stuff])

answer.sort()

print(answer)
```

```python
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
  data = list(map(int,input().split()))
  for c in range(n):
    if data[c] == 1:
      house.append((r,c))
    elif data[c] == 2:
      chicken.append((r,c))
      
candidates = list(combinations(chicken,m))

def get_sum(candidate):
  result = 0
  
  for hx, hy in house:
    temp = 1e9
    for cx, cy in candidate:
      temp = min(temp, abs(hx - cx) + abs(hy - cy))
    
    result += temp
  return result

result = 1e9
for candidate in candidates:
  result = min(result, get_sum(candidate))
  
print(result)
```