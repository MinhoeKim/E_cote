N = int(input())

array = []
for i in range(N):
  t, p = map(int, input().split())
  array.append((t,p))

p_sum_max = 0
day = 0

for t0, p0 in array:
  print(t0,p0)

  index = t0+day
  if index > len(array):
    break;
  p_sum = p0
  day += 1
  while True:
    if index > len(array)-1:
      break

    t1, p1 = array[index]
    if index == len(array)-1:
      if t1 > 1:
        break



    print('인덱스',index+1)
    
    index += t1

      
    p_sum += p1

  p_sum_max = max(p_sum_max,p_sum)
  print('썸',p_sum_max)  
print(p_sum_max)
  