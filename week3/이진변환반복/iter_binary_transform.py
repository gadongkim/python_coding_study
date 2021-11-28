def solution(s):

    index = 0
    zero = 0

    while(s != "1"):
        zero += s.count("0")
        s = ''.join([i for i in s if i =='1'])
        s = str(bin(len(s))[2:])
        index +=1
        
        solution(s)
        
    return [index, zero]