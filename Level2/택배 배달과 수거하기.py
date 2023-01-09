def solution(cap, n, deliveries, pickups):
    answer = -1
    
    d_r = []
    p_r = []
    
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
            #print("d_index--")
        #print(d, d_r, deliveries)
        
    
    return answer
