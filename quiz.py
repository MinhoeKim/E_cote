import time

int(input())
fear = list(map(int, input().split()))

start_time = time.time()

print(fear)

fear.sort(reverse = True)

print(fear)
groupnum = 0

while len(fear) != 0 :
  group = []
  while len(fear)  != 0: 
    num = fear[-1]
    temp = fear.pop()
    
    if temp > num :
      num = temp
      
    group.append(temp)

    if len(group) == num:
      groupnum += 1
      break
  
print(groupnum)
end_time = time.time()
print("time :", end_time - start_time)

#========================================

s = input()

num = [int(x) for x in s]

max_num = num[0]



for i in range(1,len(num)):
  print(max_num)
  if max_num + num[i] > max_num * num[i]:
    max_num = max_num+num[i]
  else:
    max_num = max_num*num[i]

print(max_num)

#=========================================

s = input()

count0 = 0
count1 = 0

if s[0] == 1:
  count1 += 1
else:
  count0 += 1

for i in range(len(s)-1):
  if s[i] != s[i+1]:
    if s[i] == 1 :
      count0 += 1
    else:
      count1 += 1

print(count0,count1)
print(min(count0,count1))

#=======================================

n = int(input())

coins = list(map(int, input().split()))

coins.sort()

nextmade = 1


for coin in coins:
  if nextmade < coin:
    break
    
  nextmade += coin
  

print(nextmade) 

#===================================

from itertools import combinations

n, m = map(int, input().split())

k = list(map(int, input().split()))

ball = list(combinations(k,2))

notsame = [(a,b) for a,b in ball if a != b]

print(len(notsame))

#==============================================

import heapq


k = int(input())

food_times = list(map(int, input().split()))

q = []

for i in range(len(food_times)):
  heapq.heappush(q, (food_times[i], i+1))


sum_value = 0
previous = 0

length = len(food_times)

while sum_value + ((q[0][0] - previous) * length) <= k:
  now = heapq.heappop(q)[0]
  sum_value += (now - previous) * length
  length -=1
  previous = now
 
result = sorted(q, key =lambda x: x[1])

temp = result[(k - sum_value) % length][1]
print(temp)
