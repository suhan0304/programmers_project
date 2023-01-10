#재귀 함수
def check_binary_Tree(b, d) :
    #깊이 == 1
    if d==1 :
        return 0
    
    #원소의 갯수
    n = (2**d)-1
    root_n = n//2
    left_root_n = root_n - (root_n//2+1)
    right_root_n = root_n + (root_n//2+1)
    #print(left_root_n,root_n,right_root_n)
    
    root = b[root_n]
    left_root = b[left_root_n]
    right_root = b[right_root_n]
    
    #case 1. 루트 = 0 and 자식 = 1 만들 수 없음 -> 이진트리 생성 불가
    if root == 0 and left_root == 1 or root == 0 and right_root == 1 :
        return -1
    #case 2. 루트 = 1 and 자식 = 0이든 1든 상관 없음 -> 왼쪽/오른쪽 서브트리 쪼개기
    elif root == 1 :
        #깊이는 1이 줄어듬
        return check_binary_Tree(b[:root_n-1],d-1)
        return check_binary_Tree(b[root_n+1:],d-1)
    

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
        
        check_binary_Tree(b, d)
    
    return answer

    
