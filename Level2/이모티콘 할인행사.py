import math

def solution(users, emoticons):
    answer = [0, 0]
    
    #최소 할인율 ~ 최대 할인율 구하기
    
    max_discount = 0
    min_discount = 100
    for u in users :
        #10~40%까지 10의 단위로 되기 때문에 1의 자리 숫자를 버리기 위해
        #ceil을 이용해서 올림으로 1의 자리를 없앰 
        # └ 왜 올림이냐면 내릴 경우 이모티콘 가입자가 0명으로 1번 목표에 부합하지 않음
        # └ 32%, 28% 그러면 테스트를 해야되는게 20, 30, 40% 중 20%는 테스트할 필요가 없음 = 가입자가 0명이 됨
        if math.ceil(u[0]/10) * 10 > max_discount : max_discount = math.ceil(u[0]/10) * 10
        if math.ceil(u[0]/10) * 10 < min_discount : min_discount = math.ceil(u[0]/10) * 10
        
    print(max_discount, min_discount)
    return answer
