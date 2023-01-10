def solution(numbers):
    answer = []

    binary = []
    #numbers의 숫자들을 모두 2지법으로 변환
    for i in range(len(numbers)) :
        b = ''
        while numbers[i] > 0:
            b += str(numbers[i]%2)
            numbers[i] //= 2
        b = b[::-1]
        
        #깊이를 구하는 함수 숫자 갯수가 정해져있음 (2^d - 1) 
        #깊이를 구하는 이유? 111010이면 0111010으로 이진트리 노드 갯수를 맞춰야 하기 때문에
        #깊이 → 완전 이진트리 노드 갯수 → 필요한 0을 추가할 수 있음
        #d은 이진트리의 깊이
        d = 0
        while len(b) > (2**d)-1 : 
            d+=1
        #print(d)
        #갯수 맞추기 위에 맨앞에 0 추가
        for i in range((2**d)-1-len(b)) :
            b = '0' + b
        print(b)
            
    return answer

    
