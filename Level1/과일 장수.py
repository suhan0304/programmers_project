def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m) :
        answer+=score[(i+1)*m-1]*m
    return answer
