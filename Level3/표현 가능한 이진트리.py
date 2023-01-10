def check_binary_tree(b, d) :
    
    root_n = ((2**d)-1)//2
    left_root_n = root_n//2
    right_root_n = (root_n+((2**d)-1))//2
    
    root = int(b[root_n])
    left_root = int(b[left_root_n])
    right_root = int(b[right_root_n])
     
    print(b,"/ d =",d)
    print("left_root_n=",left_root_n,"/ root_n=",root_n,"/ right_root_n=",right_root_n)
    print("left_root=",left_root,"/ root=",root,"/ right_root=",right_root)
    
    if d == 1 or (d==2 and root == 1):
        return 1
    
    if root == 0 :
        if left_root == 1 or right_root == 1 :
            return 0
    elif root == 1 :
        if check_binary_tree(b[:root_n],d-1) == 1 and check_binary_tree(b[root_n+1:],d-1) == 1:
            return 1
        else :
            return 0

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
            
        
        answer.append(check_binary_tree(b,d))
        #print("check_binary_tree",answer)
        
    return answer

    
