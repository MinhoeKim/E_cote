
string = input()

number = [int(i) for i in string if ord(i)<60 ]
print(string)
abc = [i for i in string if ord(i)>60]

abc.sort()
number = sum(number)

for i in abc:
  print(i,end='')

print(number)
