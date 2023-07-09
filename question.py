n = int(input())

card = []

for i in range(n):
    card.append(int(input()))

card.sort()

print(card)

onetwo = card[0]+card[1]
sum = 0
sum += onetwo

for i in range(2,n):

   onetwo = onetwo + card[i]
   sum += onetwo

   
print(sum)


