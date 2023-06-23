T = input()
n, m = map(int, input().split())
array = list(map(int, input().split()))

gold = []
start = 0
for i in range(n):

    gold.append(array[start:m*(i+1)])
    start += m

del_max = 0
row = None
column: None

for i in range(n):
    if del_max < gold[i][0]:
        del_max = gold[i][0]
        row = i

del_sum = 0


for j in range(m):

    if row == 0:
        del_value = max(gold[row][j], gold[row+1][j])
        del_sum += del_value
        row, column = gold.index(del_value)

    elif row == n:
        del_value = max(gold[row][j], gold[row-1][j])
        del_sum += del_value
        row, column = gold.index(del_value)

    else:
        del_value = max(gold[row][j], gold[row+1][j], gold[row-1][j])
        del_sum += del_value
        row, column = gold.index(del_value)
