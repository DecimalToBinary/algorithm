def solution(cards1, cards2, goal):
    for c in goal:
        if cards1 and cards1[0]==c:
            del cards1[0]
        elif cards2 and cards2[0]==c:
            del cards2[0]
        else:
            return "No"
    return "Yes"