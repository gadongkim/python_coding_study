def solution(s):
    answer = 0

    def check(s):

        box = []
        i = 0
        for x in s:

            if x == '(' or x =='[' or x =='{':
                box.append(x)
            elif x == ')':
                if not box:
                    return -1
                else:
                    if box[-1] != '(':
                        return -1
                    box.pop()  

            elif x == ']':
                if not box:
                    return -1
                else:
                    if box[-1] != '[':
                        return -1
                    box.pop()

            elif x == '}':
                if not box:
                    return -1
                else:
                    if box[-1] != '{':
                        return -1
                    box.pop()

        if box:
            return -1
        
        return 1

    def rotation(s):
        a_list = list(s)

        temp =  a_list[0]
        for i in range(1,len(a_list)):
            a_list[i-1] = a_list[i]
        a_list[-1] = temp

        s = "".join(a_list)
        return s

    for _ in range(len(s)):
        x = check(s)
        if x ==1:
            answer += 1

        rotation(s)
        s = rotation(s)

    return answer