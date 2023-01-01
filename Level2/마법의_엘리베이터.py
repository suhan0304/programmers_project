def solution(storey):
    
    answer = 0
    while storey > 0 :
        if storey%10 == 0 :
            storey /= 10
        elif storey%10 >= 6 :
            answer += 10 - storey%10
            storey += 10 - storey%10
        else :
            answer += storey%10
            storey -= storey%10
        
    return answer
