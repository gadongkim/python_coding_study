def solution(rows, columns, queries):
    answer = []

    arr = [[0] * columns for _ in range(rows)]
    k = 1

    for row in range(rows):
        for column in range(columns):
            arr[row][column] = k
            k+=1

    for querie in queries:
        m = rows*columns
        x1,y1,x2,y2 = querie[0]-1,querie[1]-1,querie[2]-1,querie[3]-1

        tmp = arr[x1][y1]
        m = tmp

        # 위방향, 왼쪽방향, 아래방향, 오른방향
        for x in range(x1,x2):
            arr[x][y1] = arr[x+1][y1]
            m = min(m, arr[x][y1])

        for y in range(y1,y2):
            arr[x2][y] = arr[x2][y+1]
            m = min(m, arr[x2][y])

        for x in range(x2,x1,-1):
            arr[x][y2] = arr[x-1][y2]
            m = min(m, arr[x][y2])

        for y in range(y2,y1,-1):
            arr[x1][y] = arr[x1][y-1]
            m = min(m, arr[x1][y])

        arr[x1][y1+1] = tmp

        answer.append(m)

    return answer

