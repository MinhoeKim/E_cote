```python
def find_parent(parent, 3):
    if 2 != 3:
        parent[x] = find_parent(parent, 2):
                        if 2 != 1:
                            parent[x] = find_parent(parent, 1):                                            
                                            return 1
```

```python
#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
#여행지의 개수와 여행 계획에 속한 여행지의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1)

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
  parent[i] = i

#union 연산을 각각 수행
for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1: #연결된 경우 union 연산 수행
      union_parent(parent, i+1, j+1)
      
#여행 계획 입력받기
plan = list(map(int, input().split()))

result = True
#여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m-1):
  if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
    result = False
    
#여행 계획에 속하는 모든 노드가 서로 연결되어 있는지(루트가 동일한지)확인
if result:
  print('yes')
else:
  print('no')
```

```python
G = int(input())#탑승구의 수
P = int(input())#비행기의 수

check = [0 for i in range(G+1)]#(인덱스 1 번부터 시작하기 위해 +1)
gi = []# 각 비행기가 도킹할 수 있는 탑승구의 정보(gi[i]가 3 이면 check[3] 부터 check[1])

for i in range(P):
    gi.append(int(input()))

print(check)   
for i in gi:
    out = 0 # 공항 운행 중지 조건
    for j in range(i,0,-1):#큰 탑승구의 번호부터 1번 탑승구까지 차례대로 탐색
        print(j)
        if check[j] == 0:#탑승구가 비어있으면
            check[j] = 1#비행기 도킹
            break #도킹했으면 다음 비행기 꺼내기

        if j == 1 and check[j] != 0:# 1번 탑승구까지 모두 차있으면
            out = 1 # 공항 운행 중지

    if out == 1 :
        break

result = check.count(1)# 도킹한 비행기 수

print(result)
```

```python
#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  #루트 노드가 아니라면, 루트노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

#노드의 개수와 간선의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n+1)# 부모 테이블 초기화

#모든 간선을 담을 리스트
edges = []

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,n+1):
  parent[i] = i

#모든 간선에 대한 정보를 입력받기
for _ in range(m):
  x, y ,z = map(int, input().split()) #x와 y 사이에 z길이 만큼의 도로가 있다
  # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((z, x, y))

#간선을 비용순으로 정렬
edges.sort()
total = 0 # 전체 가로등 비용
result = 0 #간선을 줄인 최종 비용
for edge in edges:
  cost, a, b = edge
  total += cost
  
  #사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(total - result)
```

```python
#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  #루트 노드가 아니라면, 루트노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

#노드의 개수 입력받기
n = int(input())
parent = [0] * (n+1) #부모 테이블 초기화

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
  parent[i] = i

x = []
y = []
z = []

#모든 노드에 대한 좌표 값 입력받기
for i in range(1, n+1):
  data = list(map(int, input().split()))
  x.append((data[0], i))
  y.append((data[1], i))
  z.append((data[2], i))

x.sort()
y.sort()
z.sort()

#인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n - 1):
  #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
  edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
  edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
  cost, a, b = edge
  #사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
```

```python
from collections import deque

# 노드의 개수 입력 받기
n = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n+1)
# 각 노드에 연결돤 간선 정보를 담기 위한 인접 행렬 초기화
graph = [[False] * (n + 1) for i in range(n+1)]
# 작년 순위 정보 입력
data = list(map(int, input().split()))
# 방향 그래프의 간선 정보 초기화
for i in range(n):
    for j in range(i+1, n):
        graph[data[i]][data[j]] = True
        indegree[data[j]] += 1

# 올해 변경된 순위 정보 입력
m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    # 간선의 방향 뒤집기
    if graph[a][b]:
        graph[a][b] = False
        graph[b][a] = True
        indegree[a] += 1
        indegree[b] -= 1
    else:
        graph[a][b] = True
        graph[b][a] = False
        indegree[a] -= 1
        indegree[b] += 1

# 위상정렬 시작
result = []  # 알고리즘 수행 결과를 담을 리스트
q = deque()  # 큐 기능을 위한 deque 라이브러리 사용

# 처음 시작할 때는 진입차수가 0 인 노드를 큐에 삽입
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

certain = True  # 위상 정렬 결과가 오직 하나인지의 여부
cycle = False  # 그래프 내 사이클이 존재하는지 여부

# 정황히 노드의 개수만큼 반복
for i in range(n):
    # 큐가 비어 있다면 사이클이 발생했다는 의미
    if len(q) == 0:
        cycle = True
        break
    # 큐의 원소가 2개 이상이라면 가능한 정렬결과가 여러 개라는 의미
    if len(q) >= 2:
        certain = False
        break
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for j in range(1, n+1):
        if graph[now][j]:
            indegree[j] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[j] == 0:
                q.append(j)
# 사이클이 발생하는 경우
if cycle:
    print("INPOSSIBLE")
# 위상 정렬 결과가 여러 개인 경우
elif not certain:
    print("?")
# 위상 정렬을 수행한 결과 출력
else:
    for i in result:
        print(i, end=' ')
    print()
```