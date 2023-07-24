from itertools import combinations

def find_length(r1,c1,field,n):
  min_length = 1e9
  for r2 in range(n):
    for c2 in range(n):
      if field[r2][c2] == 2:
        length = abs(r1 - r2) + abs(c1 - c2)
        min_length = min(min_length,length)
  return min_length

n, m = map(int, input().split())

field = []

for _ in range(n):
  field.append(list(map(int, input().split())))


chicken = []

for i in range(n):
  for j in range(n):
    if field[i][j] == 2:
      chicken.append((i,j))


selects = list(combinations(chicken, len(chicken)-m))      

min_length = 1e9

for select in selects:
  print(select)
  for x, y in select:
    field[x][y] = 0
  sum_length = 0
      
  for i in range(n):
    for j in range(n):
      if field[i][j] == 1:
        sum_length += find_length(i,j,field,n)
  min_length = min(sum_length,min_length)
  for x, y in select:
    field[x][y] = 2
print(min_length)  