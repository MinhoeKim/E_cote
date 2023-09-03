```python
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

INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

#노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현,인덱스 1을 첫번째로 하기위해 n+1)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n + 1) for _ in range(n + 1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    #자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    if a == b:
      graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  #A에서 B로 가는 비용은 C라고 설정
  a, b, c = map(int, input().split())
  #가장 짧은 간선 정보만 저장
  if c < graph[a][b]:
    graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 결과를 출력
for a in range(1, n+1):
  for b in range(1, n+1):
    # 도달할 수 없는 경우 0 을 출력
    if graph[a][b] == INF:
      print(0, end=" ")
      #도달할 수 있는 경우 거리를 출력
    else:
      print(graph[a][b], end=" ")
  print()
```

```python
INF = int(1e9)# 무한을 의미하는 값으로 10억을 설정

#노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기자신에서 자기자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
   #a에서 b로 가는 비용을 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

#점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1 , n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
          #i에서 j로 가거나 j에서 i로 가는 경로가 있으면 비교가 가능하므로 카운트해준다
            count += 1
        if count == n: #i노드가 모든노드와 비교가능하면 정확한 순위를 알 수 있다.
            result +=1

print(result)
```

```python
import heapq

INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#노드의 개수를 입력받기
n = int(input())
#전체 맵 정보를 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

#최단거리 테이블을 모두 무한을 ㅗ초기화
distance = [[INF] * n for _ in range(n)]

x, y = 0, 0
# 시작 노드로 가기 위한 비용은 (0,0) 위치의 값으로 설정하여, 큐에 삽입
q = [(graph[x][y], x, y)]
distance[x][y] = graph[x][y]

#다익스트라 알고리즘 수행
while q:
	#가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
  dist, x, y = heapq.heappop(q)
	#현재 노드가  이미 처리된 적이 있는 노드라면 무시
  if distance[x][y] < dist:
    continue
	# 현재 노드와 연결된 다른 인접한 노드들을 확인
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
		#맵의 범위를 벗어나는 경우 무시
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
      continue
		
    cost = dist + graph[nx][ny]
		#현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
    if cost < distance[nx][ny]:
      distance[nx][ny] = cost
      heapq.heappush(q, (cost, nx, ny))

print(distance[n - 1][n - 1])
```

```python
import heapq

INF = int(1e9)#무한을 의미하는 값으로 10억을 설정

#노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
#시작 노드를 1번 헛간으로 설정
start = 1
#각 노드에연결되어 있는 노드에 대한 정보를  담는 리스트를 만들기
graph = [[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
#모든 간선 정보를 입력받기
for _ in range(m):
  a,b = map(int, input().split())
  #a번 노드와 b번 노드의 이동 비용이 1이라는 의미(양방형)
  graph[a].append((b,1))
  graph[b].append((a,1))

def dijkstra(start):
  q = []
  #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:#큐가 비어있지 않다면
    #가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
    dist, now =  heapq.heappop(q)
    #현재 노드가 이미 처리된 적이 있는 노드라면 무시(우선순위 큐이므로 무한이었던 거리가
#현재 원소의 거리보다 짧아졌다는 의미는 거리가 더 짧은 경로가 나와가 이미 그 노드를 처리했다는 의미이다.) 
    if distance[now] < dist:
      continue
    #현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

#다익스트라 알고리즘 수행
dijkstra(start)

#최단 거리가 가장 먼 노드 번호(동빈이가 숨을 헛간의 번호)
max_node = 0
#도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단거리
max_distance = 0
#최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1, n+1):
  if max_distance < distance[i]:
    max_node = i
    max_distance = distance[i]
    result = [max_node]
  elif max_distance == distance[i]:
    result.append(i)

print(max_node, max_distance, len(result))
```