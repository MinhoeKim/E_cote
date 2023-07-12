n = int(input())

array = []

array.append(1)
count = 1
while len(array) <= n:
  array.append(2*count)
  array.append(3*count)
  array.append(5*count)
  array = set(array)
  array = list(array)
  count += 1
print(count)  

array = set(array)
array = list(array)
array.sort()

print(array)
print(array[n-1])