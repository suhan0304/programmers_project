def get_cds(n):
    cnt = 0
    for i in range(1, int(n**(1/2))+1): 
        if n%i == 0:
            if i == n//i: 
                cnt += 1
            else:
                cnt += 2 
    return cnt

def solution(e, starts):
    for num in range(starts,e) :
    answer = []
    return answer
