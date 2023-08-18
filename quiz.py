```python
student = [
['Junkyu', 50, 60, 100],
['Sangkeun', 80, 60, 50],
['Sunyoung', 80, 70, 100],
['Soong', 50, 60, 90],
['Haebin', 50, 60, 100],
['Kangsoo', 60, 80, 100],
['Donghyuk', 80, 60, 100],
['Sei', 70, 70, 70],
['Wonseob', 70, 70, 90],
['Sanghyun', 70, 70, 80],
['nsj', 80, 80, 80],
['Taewhan', 50, 60, 90]]

result = sorted(student,key=lambda x: (-x[1],x[2],-x[3],x[0]))

for i in result:
    print(i)

['Donghyuk', 80, 60, 100]
['Sangkeun', 80, 60, 50]
['Sunyoung', 80, 70, 100]
['nsj', 80, 80, 80]
['Wonseob', 70, 70, 90]
['Sanghyun', 70, 70, 80]
['Sei', 70, 70, 70]
['Kangsoo', 60, 80, 100]
['Haebin', 50, 60, 100]
['Junkyu', 50, 60, 100]
['Soong', 50, 60, 90]
['Taewhan', 50, 60, 90]
```

```python
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])

 이 문제의 핵심 아이디어는 정확히 중간값에 해당하는 위치의 집에 안테나를 설치했을 때,
 안테나로부터 모든 집까지의 거리의 총합니 최소가 된다는 점이다.
 1 2 3 5 8 9
 이 때, 중간값에 해당하는 위치인 3 혹은 5ㅇㅔ 안테나를 설치하는 경우, 안테나로부터
 모든 집까지의 거리의 총합이 최소가 된다.
```

```python
n = int(input())

stages = list(map(int, input().split()))

stages.sort()

per = []
remain_user = 0
passed_user = len(stages)

for i in range(1,n+1):
    remain_user = stages.count(i)
    #해당 스테이지에 머물러 있는 유저의 숫자를 카운트한다.
    per.append((i,remain_user/passed_user))
    #머물러있는 유저를 통과한 유저의 수로 나눈 것이 실패율이므로 per에 스테이지와 함께 넣어준다
    passed_user -= remain_user
    #다음 스테이지의 실패율 계산을 위해 현재 스테이지의 남아있는 유저 수를 빼준다
per = sorted(per, key=lambda x:x[1], reverse=True) #내림차순

answer = [i[0] for i in per]    

print(answer)
```

```python
n = int(input())

card = []

for i in range(n):
    card.append(int(input()))

card.sort()
#작은 순서대로 정렬 후 더해 나가는 것이 최솟값이다.
print(card)

onetwo = card[0]+card[1]
#최초 시작값 원투
sum = 0
sum += onetwo
#원투를 총합에 더해준다.
for i in range(2,n):
   onetwo = onetwo + card[i]
   #총합에 더해 주었으면 바로 뒤에있는 카드를 더해주어 원투를 갱신한다.
   sum += onetwo
   #원투를 총합에 더해준다
print(sum)
```