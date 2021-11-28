
s = '{{}}{}'
    


def solution(s):
    index = 0


    def rotation(s):
        a_list = list(s)

        temp =  a_list[0]
        for i in range(1,len(a_list)):
            a_list[i-1] = a_list[i]
        a_list[-1] = temp

        s = "".join(a_list)

        return s

    for i in range(len(s)):
        rotation(s)
        s = rotation(s)
        print(s,i,'번째 회전')

    return s

print(solution(s))


