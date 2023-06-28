string = input()

number = [int(i) for i in string]

sum = number[0]
for i in range(len(number)-1):
	
	temp = max((sum*number[i+1], (sum+number[i+1])))
	
	if temp == sum*number[i+1]:
		sum = sum*number[i+1]
	else:
		sum = sum+number[i+1]
		
print(sum)
