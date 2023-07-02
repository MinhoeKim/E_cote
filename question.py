G = int(input())
P = int(input())

gi = []
check = [0 for i in range(G+1)]



for i in range(P):
    gi.append(int(input()))
    


print(check)   
for i in gi:
    out = 0
    for j in range(i,0,-1):
        print(j)
        if check[j] == 0:
            check[j] = 1
            break
        
        if j == 1 and check[j] != 0:
            out = 1
            
    if out == 1 :
        break
    
result = check.count(1)

print(result)  

