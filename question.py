words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']

queries = ['fro??', '????o', 'fr???', 'fro???', 'pro?']

answer = [0,0,0,0,0]

for i in range(len(queries)):
    query = queries[i]
    count = query.count('?')
    length = len(query)
    first = query[0]
    if first == '?':
        temp = query[count:]
        for word in words:
            if len(query)==len(word) and word[count:] == temp:
                answer[i] += 1
    else:
        temp = query[:len(query)-count]
        for word in words:
            if len(query) == len(word) and word[:len(query)-count] == temp:
                answer[i] += 1
                
print(answer)
        