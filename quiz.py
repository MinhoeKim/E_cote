```python
T = int(input())

while T != 0:
    n, m = map(int, input().split()) #행, 열
    array = list(map(int, input().split()))

    gold = []
    start = 0
    #금광이 한줄로 입력되므로 2차원배열로 변환
    for i in range(n):
        gold.append(array[start:m*(i+1)]) #i번째 행 추가
        start += m #다음 행의 시작점

    row = None

    del_max = 0
    #맨 처음 열에서 가장 큰 수를 시작점으로 한다
    for i in range(n):
        if del_max < gold[i][0]:
            del_max = gold[i][0]
            row = i

    del_sum = del_max

    #열의 갯수만큼 반복
    for j in range(1,m):
        if row == 0: # 맨 처음 행일때
            compare = []
            compare.extend([gold[row][j], gold[row+1][j]])#다음 열의 중간쪽,위쪽 비교하기 위해 리스트 형태로 넣어준다
            del_value = max(compare)
            del_sum += del_value
            max_index =  compare.index(del_value)

            row = row + max_index #다음 열과 비교하기위한 현재 최대값의 행 위치

        elif row == n-1: #맨 마지막 행일때
            compare = []
            compare.extend([gold[row-1][j],gold[row][j]])#다음열의 아래쪽 중간쪽 비교, append는 하나의 원소만 넣을 수 있으므로 extend를 이용해 리스트로 넣어준다
            del_value = max(compare)
            del_sum += del_value
            max_index =  compare.index(del_value)

            row = row + max_index -1#다음 열과 비교하기위한 현재 최대값의 행 위치

        else:#처음과 마지막 사이일 때
            compare = []
            compare.extend([gold[row-1][j],gold[row][j],gold[row+1][j]]) #다음 열의 위쪽, 중간쪽, 아래쪽 비교
            del_value = max(compare)
            del_sum += del_value
            max_index =  compare.index(del_value)

            row = row + max_index -1#다음 열과 비교하기위한 현재 최대값의 행 위치

    print(del_sum)

    T -= 1
```

```python
n = int(input())
tower = []
for i in range(n):
    tower.append(list(map(int, input().split())))

temp = [[]]# 1행부터 시작하기 위해 0행을 빈 리스트로 초기화한다

for i in range(n-1):# 마지막 줄을 빼고 템프에 저장
    temp.append(tower[i])

for i in range(n-1, 0, -1): #n-1부터  1까지 -1스텝으로 진행 (행)
    for j in range(len(tower[i])-1):#j를 (타워행의길이-1)한만큼 반복 (열)
        if tower[i][j] > tower[i][j+1]:#현재 원소가 다음 원소의 값보다 크면
            temp[i][j] = tower[i][j]+temp[i][j]#부모 노드를 큰값과 더한 값으로 갱신한다
        else:
            temp[i][j] = tower[i][j+1]+temp[i][j]#부모 노드를 큰값과 더한 값으로 갱신한다

print(*temp[1])# 루트 노드를 출력
```

```python
N = int(input())

array = []
for i in range(N):
  t, p = map(int, input().split())
  array.append((t,p))
z = len(array)
p_sum_max = 0#최대 수익
day = 0 #처음 일을 시작할 날짜

for t0, p0 in array: #일의 시간, 수익
  
  index = day #현재 일을 시작할 날짜
  day += 1 #다음루프를 위해 일을 시작할 날짜를 1 증가시킨다.
  p_sum = 0#일을 시작한 날짜의 총 수입
  
  if day+t0 > len(array)-1:# 다음 일의 위치의 인덱스가 초과된다면
    break
  else:#초과되지 않는다면
    p_sum += p0# 현재 일의 수익을 더해준다
    index += t0 #현재 일을 시작한 날짜에 수행시간을 더해 다음 일의 인덱스를 구한다
    
  while True:
    if index > len(array)-1:#현재 인덱스가 범위를 초과하면
      break
    else:#초과하지 않는다면
      t1, p1 = array[index]#array[index]의 일의 시간, 수익
      
    if index == len(array)-1:#마지막번재 인덱스이고
      
      if t1 > 1:#일이 하루넘게 걸린다면
        break
      else:#하루 넘게 걸리지 않는다면
        p_sum += p1#수행한 일의 수익을 더해준다
        index += t1#일을 수행하고 난 후 다음있을 일의 인덱스
        
    else:#마지막 번째 인덱스가 아니라면
      p_sum += p1#수행한 일의 수익을 더해준다
      index += t1#일을 수행하고 난 후 다음있을 일의 인덱스

  p_sum_max = max(p_sum_max,p_sum)#시작한 일의 날짜들 중에서 최댓값을 구한다
  
print(p_sum_max)
```

```python
n = int(input())

soldier = list(map(int, input().split()))

count = 0

for i in range(len(soldier)-1):
  pre = soldier[i]
  next = soldier[i+1]
  if pre < next:
    count +=1

print(count)
```

```python
n = int(input())

array = []

array.append(1)
count = 1
while len(array) <= n:  # 원소의 갯수가 n보다 작거나 같으면 2,3,5 의 배수를 append
    array.append(2*count)
    array.append(3*count)
    array.append(5*count)
    array = set(array)  # 중복제거
    array = list(array)  # 다시 리스트 변환
    count += 1
print(count)

array.sort()

print(array)
print(array[n-1])#n번째 못생긴 수 출력
```


#최소 편집 거리 계산을 위한 다이나믹 프로그래밍
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    #다이나믹 프로그래밍을 위한 2차원 dp테이블초기화
    dp = [[0] * (m+1) for _ in range(n+1)]

    #dp테이블 초기 설정
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    #최소 편집거리 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            #문자가 같다면, 원쪽 위에 해당하는 수를 그대로 대입
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            #문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else:#삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서  최소 비용을 찾아 대입
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))
```