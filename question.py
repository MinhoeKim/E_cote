def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

array = [[0,0,0,0,0,0]]


for i in range(N):
    temp = [0]
    temp.extend(map(int, input().split()))
    array.append(temp)

print(array)


parent = [0]*(N+1)

for i in range(N+1):
    parent[i] = i
print(parent)    


for i in range (1,N+1):
    for j in range (1,N+1):
        if array[i][j] == 1:
            union_parent(parent,i,j)
            
print(parent)

input_node = list(map(int,input().split()))

select = []
print(input_node)

for i in input_node:
    select.append(parent[i])

result = set(select)

print(result)

if len(result) == 1:
    print('Yes')
else:
    print('No')