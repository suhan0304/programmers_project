
def solution(e, starts):
    answer = []
    
    divisor=[0 for i in range(e+1)]
    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)):
            divisor[i*j]+=2
    for i in range(1,int(e**(1/2))+1):
        divisor[i**2]+=1
    
    
    for i in range(len(starts)) :
        print(divisor[starts[i]:e+1])
        n = max(divisor[starts[i]:e+1])
        print(n,divisor.index(n,starts[i],e+1))
        answer.append(divisor.index(n,starts[i],e+1))
    return answer
