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
length = [0]*(n+1)

bfs(graph, x, visited, length)

if not k in length:
    print(-1)

for i in range(len(length)):
    if length[i] == k:
        print(i)
        


