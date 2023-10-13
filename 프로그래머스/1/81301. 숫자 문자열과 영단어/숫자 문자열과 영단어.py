# dict 자료구조를 이용해 배열의 구성 바꾸기: 배열에 key에 속하는 item이 있으면 value로 대체하는 문제
# items(), replace() 그리고 dict의 활용법 **
def solution(s):
    dict={"zero":'0',"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}
    for key,num in dict.items():
        if key in s:
            s=s.replace(key,num)
    
    return int(s)