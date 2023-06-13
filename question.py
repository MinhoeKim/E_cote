module_variable = 0

def binary_search(array, target, start, end):
    
    if start > end:
        return None
    
    mid = (start + end)//2
    
    global module_variable
    
    if array[mid] == target:
        module_variable += 1
    
    binary_search(array, target, start, mid-1)
    
    binary_search(array, target, mid+1, end)
    
    

N, x = map(int, input().split())

array = list(map(int, input().split()))

binary_search(array,x,0,N-1)

if module_variable == 0:
    print(-1)
else:
    print(module_variable)

