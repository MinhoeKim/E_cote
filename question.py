S= input()

number = [int(i) for i in S]

count0 = 0
count1 = 0

for i in range(len(S)-1):
  if number[i] != number[i+1]:
    if number[i] == 0:
      count0 += 1
    else:
      count1 += 1

result = min(count0,count1)

print(result)

