def solution(price, money, count):
    total = 0

    for i in range(1,count+1):
        new_price = price*i;
        total += new_price;
        
    return abs(total-money)

    