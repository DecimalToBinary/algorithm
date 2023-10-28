# hash 자료형 key 이용해 정렬하기
# sorted(dict.items()) >> key 기준으로 정렬된 dict의 키, 값의 쌍으로 이루어진 튜플의 집합 반환
# .. hash를 (key, key가 numbers내에서 처음 등장하는 위치의 인덱스 값)의 쌍으로 구성해 풀려고 했으나 너무 복잡해져 실패... heap을 이용해 풀이함. hash로는 풀 방법이 없는걸까?

from heapq import heappop,heappush

def solution(numbers):
    result = [-1 for _ in range(len(numbers))]
    heap = [(numbers[0],0)]
    for i,n in enumerate(numbers[1:]):
        while heap and heap[0][0]<n:
            _,idx = heappop(heap)
            result[idx] = n
        heappush(heap,(n,i+1))
    return result