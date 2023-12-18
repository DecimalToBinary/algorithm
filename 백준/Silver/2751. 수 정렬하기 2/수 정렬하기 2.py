# input()과 sys.stdin.readline()의 차이점 : 입력이 매우 클때 후자가 전자보다 빠르다. 왜?
# input(prompt) : prompt 메세지 기본 출력, 개행문자 삭제한 값을 리턴해 느림

import sys

N = int(input())
l = []
for i in range(N):
    l.append(int(sys.stdin.readline()))
    
l.sort()
for i in range(N):
    print(l[i])