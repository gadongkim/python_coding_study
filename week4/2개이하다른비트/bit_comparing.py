def solution(numbers):
    answer = []

    for number in numbers:
        s = list(bin(number)[2:])
        k = number+1

        while True:
            if (k-number)%2 == 0: count = 0
            else: count = 1

            k2 = list(bin(k)[2:])

            # 1. 주어진 넘버와 비교 숫자 길이 같게 만들기
            if len(k2) != len(s):
                while len(k2)-len(s):
                    s.insert(0,0)
                    
            # 2. 비교 숫자 길이동안 한 인덱스씩 비교해서 count하기
            for i in range(len(k2)-1):
                if k2[i] != s[i]:
                    count += 1
                    
            # 비교 숫자가 비트개수 2 이하일 경우에는 answer에 추가하고 while문 벗어나기
            if count <= 2:
                answer.append(k)
                break

            k+= 1

    return answer

# print(solution([3,7]))