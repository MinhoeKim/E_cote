food_times = list(map(int,input().split()))
k = int(input())

result = 0
index = 0
while True:
  
  print(k)
  i = index % len(food_times)
  if food_times[i] != 0:
    food_times[i] -= 1
    result = i
    k -= 1
    index += 1
  elif food_times[i] == 0:
    index += 1
  print(food_times)
  if k < 0:
    break

  if len(set(food_times)) <= 1:
    break


print(result)