def solution(players, callings):
    
    r={player:i for i,player in enumerate(players)}
    for who in callings:
        idx=r[who]
        r[who]-=1
        r[players[idx-1]]+=1
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
    return players