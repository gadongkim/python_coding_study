def solution(n):
    c = 1
    answer = [[0]*i for i in range(1,n+1)]
    
    for i in range(1,n+1):
        # a는 몫, b는 나머지
        a,b = divmod(i,3)

        # 아래방향으로 1씩 늘어나는 turn
        if(b==1):
            x = 2*a
            y = a
            for _ in range(n-i+1):
                answer[x][y] = c 
                c+=1
                x+=1

        # 오른쪽방향으로 1씩 늘어나는 turn
        elif(b==2):
            x = n-a-1
            y = a+1

            for _ in range(n-i+1):
                answer[x][y] = c 
                c+=1
                y+=1


        # 대각선 역방향으로 1씩 늘어나는 turn
        elif(b==0):
            x = n-1-a
            y = n-2*a

            for _ in range(n-i+1):
                answer[x][y] = c 
                c+=1
                y-=1
                x-=1
    
    answer = sum(answer,[])
    return answer