def solution(n):
    answer = 2;
    if(n%2 != 0) : 
        return answer;
    else :
        for i in range(3,n,2):
            if(n%i==1): break;
        return i;