from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_r = deque()
    p_r = deque()
    
    d_index = p_index = n - 1
    d = p = cap
    
    while d_index > -1 :
        if deliveries[d_index] > 0 :
            if d == cap :
                d_r.append(d_index+1)
            deliveries[d_index] -= 1
            d -= 1
            if d == 0 : d = cap
        else :
            d_index -= 1
    
    while p_index > -1 :
        if pickups[p_index] > 0 :
            if p == cap :
                p_r.append(p_index+1)
            pickups[p_index] -= 1
            p -= 1
            if p == 0 : p = cap
        else :
            p_index -= 1
    
    #print(d_r, p_r)
    
    if len(d_r) > 0 and len(p_r) > 0 :
        min_len = len(d_r) if len(d_r) < len(p_r) else len(p_r)
        for _ in range(min_len) :
            d_last = d_r.popleft()
            p_last = p_r.popleft()
            answer += 2 * (p_last if p_last > d_last else d_last)
        while len(d_r) > 0:
            answer += 2 * d_r.popleft()
        while len(p_r) > 0:
            answer += 2 * p_r.popleft()
    return answer
