#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 2;
    if(n%2!=0) return answer;
    else{
       for(int i=3; i<n; i+=2){
           if(n%i==1){
               answer = i;
               break;
            }
       }
    return answer;
    }
       
}