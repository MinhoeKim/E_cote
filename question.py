n = int(input())

soldier = list(map(int, input().split()))

count = 0

for i in range(len(soldier)-1):
  pre = soldier[i]
  next = soldier[i+1]
  if pre < next:
    count +=1

print(count)