```python
from collections import deque

def bfs(graph, start, visited, length):
    queue = deque([start])
    visited[start] = True
    length[start] = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                length[i] = length[v]+1

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
	              virus(nx, ny)

for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            array[i][j] = 1
            count += 1
            dfs(count)
            array[i][j] = 0
            count -= 1

while q:
  virus, s, x, y = q.popleft()
  if s == target_s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s+1, nx, ny))
```

```python
from collections import deque

def bfs(graph, start, visited, length):
    queue = deque([start])
    visited[start] = True
    length[start] = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                length[i] = length[v]+1

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):

    index, num = map(int, input().split())
    graph[index].append(num)

visited = [False]*(n+1)
length = [1e9]*(n+1)

bfs(graph, x, visited, length)

if not k in length:
    print(-1)

for i in range(len(length)):
    if length[i] == k:
        print(i)
====================================================================

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
  now = q.popleft()

for next_node in graph[now]:
  if distance[next_node] == -1:
    distance[next_node] = distance[now] + 1
    q.append(next_node)

check = False
for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    check = True

if check == False:
  print(-1)
```

```python
n, m = map(int, input().split())
array = []
temp = [[0]*m for _ in range(n)]

for i in range(m):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score +=1

    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = array[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)

        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                array[i][j] = 1
                count += 1
                dfs(count)
                array[i][j] = 0
                count -= 1

dfs(0)
print(result)
```

```python
from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s,target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0,1,0,-1]

while q:
  virus, s, x, y = q.popleft()
  if s == target_s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])
```

```python
def Balance_s(w):
    countL = 0
    countR = 0
    countL += w.count('(')
    countR += w.count(')')

    return countL, countR

def Right_s(s):
    count = 0

    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1

        if count < 0:
            return False

    return True

def Separate(w):
    count_L, count_R = Balance_s(w)
    
    s = ''
    if count_L == count_R:#문자열 w 가 균형잡힌 괄호 문자열이라면 실행
        for i in range(1, len(w)+1):
            print(w[:i])
            L, R = Balance_s(w[:i])
            #문자열 w를 두 '균형잡힌 괄호 문자열' u,v로 분리합니다. 단,u는'균형잡인 괄호 문자열'
            #로 더 이상 분리할 수 없어야 하며,v는 빈 문자열이 될 수 있습니다.
            if L == R:
                u = w[:i]
                v = w[i:]
                if Right_s(u) == True:
                  #문자열 u가 '올바른 괄호 문자열'이라면 문자열 v에 대해
                  #1단계부터 다시 수행합니다.
                    s += w[:i]
                    s += Separate(v)
                    # 더 이상 분리할수 없어야 하는 것은 for 문에서 최소값이므로 break로 끊어주기
                    break
                else:
                  #문자열 u가'올바른 괄호 문자열'이 아니라면 아래 과정을 수행합니다.
                  #빈 문자열에 첫번째 문자로 '('를 붙입니다.
                  #문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
                  #')'다시 붙입니다.
                  #u의 첫번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
                  #생성관 문자열을 반환합니다.
                    s += '('
                    s += Separate(v)
                    s += ')'

                    temp = u[1:len(u)-1]

                    for i in temp:
                        if i == '(':
                            s += ')'
                        else:
                            s += '('
                    # 더 이상 분리할수 없어야 하는 것은 for 문에서 최소값이므로 break로 끊어주기
                    break
            else:
                continue

    return s

s = '()))((()'

print(Separate(s))
```

```python
n = int(input())

data = list(map(int, input().split()))

add, sub, mul, div = map(int,input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
  global min_value, max_value, add, sub, mul, div

  if i == n:#숫자 사이에 모두 연산자를 끼워 넣었을 때,
    min_value = min(min_value, now)
    max_value = max(max_value, now)
    print('index', i)
    print('min',min_value)
    print('max',max_value)

  else:
    #n이 3이고,
    #add, sub, mul, div 가 2, 0, 2, 0 일때, 2,0,0,0 부터 1,0,1,0 => 0,0,2,0 까지 순서대로 값을 확인한다.
    if add > 0:
      add -= 1
      print('index', i)
      print('add',add)
      print('mul',mul)
      dfs(i+1, now + data[i])
      add += 1
    if sub > 0:
      sub -= 1
      print('sub')
      dfs(i+1, now - data[i])
      sub +=1
    if mul > 0:
      mul -= 1
      print('index', i)
      print('add',add)
      print('mul',mul)
      dfs(i + 1, now * data[i])
      mul += 1
    if div >0:
      div -= 1
      print('div')
      dfs(i + 1, int(now / data[i]))
      div += 1

dfs(1, data[0])

print(max_value)
print(min_value)
```

```python
n = 5

array = [['X','S','X','X','T'],
        ['T','X','S','X','X'],
        ['X','X','X','X','X'],
        ['X','T','X','X','X'],
        ['X','X','T','X','X']]
temp = [[0] * n for _ in range(n)]

#for _ in range(n):
    #array.append(list(input().split()))

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
debug_one = 0
debug_two = 0
debug_three = 0

def dfs(count):
    global student
    global result
    global debug_one
    global debug_two
    global debug_three

    if count == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = array[i][j]

        for i in range(n):
            for j in range(n):
                if temp[i][j] == 'T':
                    view(i, j)

        if student == 3:
            result = 'yes'

        else:
            student = 3
       

        return
    for i in range(n):
        for j in range(n):

                
            if array[i][j] == 'X':
                array[i][j] = 'O'
                count += 1
                
                #재귀함수 디버깅
                # if count == 1  and i == 0 and j == 3:
                #     debug_one = 1
                
                # if debug_one == 1 and count == 2 and i == 1 and j == 1:
                #     debug_two = 1
                  
                # if debug_two == 1 and count == 3 and i == 2 and j == 2:
                #     debug_three = 1
                  
                # if debug_one == debug_two == debug_three == 1:
                #     print()
                #     print(array)
                #     print(temp)
                    

                dfs(count)

                array[i][j] = 'X'
                count -= 1
                

dfs(0)
print(result)
```

```python
from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index, union):
  united = []
  united.append((x,y))
    #인구이동이 일어난 인덱스 리스트
  q = deque()
  q.append((x,y))
    #조사할 인덱스 큐
  union[x][y] = index
    #조사한 위치를 표시
  summary = graph[x][y]
  count = 1

  while q:
      #조사를 해야할 인덱스 큐가 비어있을때 까지
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
          #범위를 벗어나지 않고 아직 처리가 되지 않았으면 
        if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
          q.append((nx,ny))
          #인구 차이가 l,r 사이이면 q에 집어넣는다
          union[nx][ny] = index
          #조사한 위치를 표시 
          summary += graph[nx][ny]
          #인구이동 후 평균값을 계산하기위해 더해준다
          count += 1
          #인구이동이 일어난 나라를 증가시킨다
          united.append((nx,ny))
          #인구이동이 일어난 인덱스를 넣어준다

  for i,j in united:
    graph[i][j] = summary//count
  return count

total_count = 0

while True:
  union = [[-1] * n for _ in range(n)]
  index = 0
  for i in range(n):
    for j in range(n):
      if union[i][j] == -1:
        #아직 인덱스를 조사하지 않았으면
        process(i, j, index, union)
        index += 1
  if index == n*n:
      #모든 인덱스를 조사하였을 때 인구이동이 없으면
    break
  total_count += 1
  #모든 인덱스를 조사하였을 때 인구이동이 있으면

print(total_count)
```