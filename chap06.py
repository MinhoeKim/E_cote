# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(1, len(array)):
#     for j in range(i, 0, -1):

#         jj = j-1
#         if array[j] < array[j - 1]:
#             array[j], array[j - 1] = array[j - 1], array[j]
#         else:
#             break

# print(array)

# ===================================================

# n = int(input())

# array = []
# for i in range(n):
#     array.append(int(input()))

# array = sorted(array, reverse=True)

# for i in array:
#     print(i, end=' ')

# =======================================================

# n = int(input())

# array = []
# for i in range(n):
#     input_data = input().split()

#     array.append((input_data[0], int(input_data[1])))

# array = sorted(array, key=lambda student: student[1])

# for student in array:
#     print(student[0], end=' ')

# =========================================

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# a.sort()
# b.sort(reverse=True)

# for i  in range(k):
#     if a[i] < b[i]:
#         a[i], b[i] = b[i], a[i]
    
#     else:
#         break
    
# print(sum(a))

#================================================

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid - 1
            
        else:
            start = mid + 1
    
    return None

# n = int(input())

# array = list(map(int, input().split()))
# array.sort()

# m = int(input())

# x = list(map(int, input().split()))


# for i in x:
    
#     result = binary_search(array, i, 0, n - 1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

#==========================================

# n = int(input())
# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1
    
# m = int(input())

# x = list(map(int, input().split()))

# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

#================================
# n = int(input())

# array = set(map(int, input().split()))

# print(array)

# m = int(input())

# x = list(map(int, input().split()))

# for i in x:
    
#     if i in array:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

#================================================

n, m = list(map(int, input().split(' ')))

array = list(map(int, input().split()))


start = 0
end = max(array)


result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
        
    else:
        result = mid
        start = mid + 1
        
print(result)