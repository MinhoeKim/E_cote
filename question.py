s = input()

answer = len(s)

for i in range(1,len(s)):
    str_temp = s[0:i]
    count = 1
    compressed = ''
    for j in range(i, len(s), i):
        
        # if i+j >= len(s)+1:
        #     compressed += str(count) + s[j:]
        #     break
        
        if str_temp == s[j:j+i]:
            count += 1
            
        else: 
            compressed += str(count) + str_temp if count >= 2 else str_temp
            str_temp = s[j:j+i]
            count = 1
        
        if j+i >= len(s):
            compressed += str(count) + str_temp if count >= 2 else str_temp
            break


    print(compressed)        
    answer = min(answer,len(compressed))

print(answer)