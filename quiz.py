```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    #해당값의 오른쪽 인덱스를 반환
    right_index = bisect_right(array, right_value)
    #해당값의 왼쪽 인덱스를 반환
    left_index =  bisect_left(array, left_value)
    #오른쪽 인덱스- 왼쪽 인덱스는 해당 인덱스 시작과 끝에 있는 값의 갯수이다
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)
```

```python
def binary_search(array: list[int], start, end):
    while start <= end:
        mid = (start + end)//2

        if array[mid] == mid: #해당 값이 인덱스와 같으면
            return mid
        elif array[mid] > mid: #인덱스가 해당 값보다 작으므로 인덱스보다 작은 범위에서 찾는다 
            end = mid - 1
        else:
            start = mid + 1 #인덱스가 해당 값보다 크므로 인덱스보다 큰 범위에서 찾는다
    return None

N = int(input())

array = list(map(int, input().split()))

result = binary_search(array, 0, len(array)-1)

if result == None:
    print(-1)
else:
    print(result)
```

```python
N, C = map(int, input().split())

x = []
for i in range(N):
    x.append(int(input()))

x.sort()# 이진 탐섹을 위한 공유기 좌표 정렬

start = 1 # 가능한 최소거리(min gap)
end = x[-1] - x[0]# 가능한 최대 거리(max gap)
result = 0

while start <= end :
    mid = (start+end)//2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
    value = x[0]
    count = 1
    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1,N): # 앞에서 부터 차근차근 설치
        if x[i] >= value+mid:
            value = x[i]
            count += 1

    if count >= C: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 감소
        start = mid +1
        result = mid #최적의 결과를 저장
    else:# C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid -1

print(result)
```

```python
words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']

queries = ['fro??', '????o', 'fr???', 'fro???', 'pro?']

answer = [0,0,0,0,0]

for i in range(len(queries)):
    query = queries[i]
    count = query.count('?')
    length = len(query)
    first = query[0]
    if first == '?':
        temp = query[count:]
        for word in words:
            if len(query)==len(word) and word[count:] == temp:
                answer[i] += 1
    else:
        temp = query[:len(query)-count]
        for word in words:
            if len(query) == len(word) and word[:len(query)-count] == temp:
                answer[i] += 1
                
print(answer)
```