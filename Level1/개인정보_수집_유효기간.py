import re

def solution(today, terms, privacies):
    answer = []
    term = {}
    today = list(map(int, today.split('.')))
    days = (today[0]-2000) * 28 * 12 + today[1] * 28 + today[2]
    #print("days = ",days)
    for t in terms :
        term[re.split(' ',t)[0]] = int(re.split(' ',t)[1])
    for privacy in privacies :
        p = re.split('[ .]',privacy)
        p[:3] = list(map(int,p[:3]))
        p_days = ((p[0]-2000) * 28 * 12 + p[1] * 28 + p[2]) + term[p[3]] * 28 
        #print("privacy days = ",p_days)
        if days >= p_days :
            answer.append(privacies.index(privacy)+1)
    return answer
