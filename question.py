T = int(input())

while T != 0:
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    gold = []
    start = 0
    for i in range(n):

        gold.append(array[start:m*(i+1)])
        start += m


    row = None

    del_max = 0
    for i in range(n):
        if del_max < gold[i][0]:
            del_max = gold[i][0]
            row = i


    del_sum = 0


    for j in range(m):

        if row == 0:
            compare = []
            compare.extend([gold[row][j],gold[row+1][j]])
            del_value = max(compare)
            del_sum += del_value
            max_index =  compare.index(del_value)
            
            row = row + max_index

        elif row == n-1:
            compare = []
            compare.extend([gold[row-1][j],gold[row][j]])
            del_value = max(compare)
            del_sum += del_value
            max_index =  compare.index(del_value)
            
            row = row + max_index -1

        else:
            compare = []
            compare.extend([gold[row-1][j],gold[row][j],gold[row+1][j]])
            del_value = max(compare)
            del_sum += del_value
            max_index =  compare.index(del_value)
            
            row = row + max_index -1
        
        
    print(del_sum)
    
    T -= 1