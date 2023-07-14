#a : 0은 기둥, 1은 보
#b : 0은 삭제, 1은 설치
n = int(input())

build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
#build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]


build = [[' ']*(n+2) for i in range(n+2)]

re_frame = []

for frame in build_frame:
  
  x, y, a, b = frame
  if b == 1:
    if a == 0:
      if y == 0 or build[y][x-1] == '-' or build[y][x+1] == '-' or build[y-1][x] == 'I':
        build[y][x] = 'I'
      else:
        continue
    else:
      if build[y-1][x] == 'I' or build[y][x-1] == '-' or build[y][x+1] == '-':
        build[y][x] = '-'
      else:
        continue
      
  else:
    if a == 0:
      if y == 0 or build[y][x-1] == '-' or build[y][x+1] == '-' or build[y-1][x] == 'I':
        build[y][x] = ' '
      else:
        continue
    else:
      if build[y][x-1] == '-' and build[y][x+1] == '-':
        build[y][x] = '-'
      else:
        build[y][x] = ' '


      
  
    
for i in range(n+1):
  for j in range(n+1):
    if build[i][j] != ' ':
      re_frame.append([j,i,build[i][j]])

re_frame.sort()
print(build)
print(re_frame)