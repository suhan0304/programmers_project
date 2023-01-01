def solution(s):
    answer = []
    st = {}
    for i in range(len(s)) :
        if st.get(s[i],-1) == -1 : # not in dict
            answer.append(-1) 
            st[s[i]] = i+1
        else :
            answer.append(i+1-st[s[i]])
            st[s[i]] = i+1
    print(st)
    return answer
