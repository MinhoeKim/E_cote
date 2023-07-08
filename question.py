def Balance_s(w):
    countL = 0
    countR = 0
    countL += w.count('(')
    countR += w.count(')')

    return countL, countR


def Right_s(s):
    count = 0

    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1

        if count < 0:
            return False

    return True


def Separate(w):
    count_L, count_R = Balance_s(w)
    s = ''
    if count_L == count_R:
        for i in range(1, len(w)+1):
            print(w[:i])
            L, R = Balance_s(w[:i])
            
            if L == R:
                u = w[:i]
                v = w[i:]
                if Right_s(u) == True:
                    s += w[:i]
                    s += Separate(v)
                    # break로 끊어주기
                    break
                else:
                    s += '('
                    s += Separate(v)
                    s += ')'

                    temp = u[1:len(u)-1]

                    for i in temp:
                        if i == '(':
                            s += ')'
                        else:
                            s += '('
                    # break로 끊어주기
                    break
            else:
                continue

    return s


s = '()))((()'

print(Separate(s))
