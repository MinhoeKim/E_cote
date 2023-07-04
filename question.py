n = int(input())

stages = list(map(int, input().split()))

stages.sort()


per = []
count = 0
length = len(stages)

for i in range(1,n+1):
    count = stages.count(i)
    
    per.append((i,count/length))
    
    length -= count

per = sorted(per, key=lambda x:x[1], reverse=True)

answer = [i[0] for i in per]    

print(answer)
    
     
        