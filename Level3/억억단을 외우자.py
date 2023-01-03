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
    answer = []
    for i in range(len(starts)) :
        max_n = 0
        flag = 0
        for j in range(starts[i],e+1) :
            #print(j)
            if get_cds(j) > max_n :
                max_n = get_cds(j)
                flag = j
        answer.append(flag)
    return answer
