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
    
    #최소 할인율 ~ 최대할인율까지 각 이모티콘 별 모든 할인율 조합
    com = []
    stack = [[]]
    while len(stack) > 0 :
        simul = stack.pop() 
        if len(simul) >= len(emoticons) :
            com.append(simul)
            continue
        for d in range(min_discount, max_discount+10,10) :
            stack.append(simul + [d])
    #print(max_discount, min_discount)
    
    for c in range(len(com)) :
        answer2 = [0, 0]
        for u in users :
            bill = 0
            for i in range(len(emoticons)) :
                #할인율이 사용자가 원하는 할인율보다 크면 결제금액에 추가
                if u[0] <= com[c][i] :
                    bill += emoticons[i] * (100 - com[c][i]) / 100
            #할인하는 이모티콘 모두 구매하기 위한 결제금액이 자신의 기준가를 넘어가면
            #이모티콘 플러스 서비스를 가입함
            if bill >= u[1] :
                answer2[0] += 1
            #기준가를 안넘어가면 그냥 이모티콘을 별도 구매하는 것이기 때문에
            #총 이모티콘 판매액이 그만큼 증가함
            else :
                answer2[1] += int(bill)
            #print(bill)
            #각 조합마다 가입자의 수와 이모티콘 판매액을 모두 비교해서 목표 1, 2번에 부합하는 답을 추출함
            if answer2[0] > answer[0] or (answer2[0] == answer[0] and answer2[1] > answer[1]) :
                answer = answer2
            
                
                
    return answer
