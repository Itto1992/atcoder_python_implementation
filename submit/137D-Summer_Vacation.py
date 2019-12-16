
import sys
import heapq
from collections import defaultdict


def main():
    input = sys.stdin.readline
    
    N, M = map(int, input().split())

    table = defaultdict(list)
    for i in range(N):
        A, B = map(int, input().split())
        table[A].append(-B)

    candidate = []
    heapq.heapify(candidate)

    ret = 0

    for i in range(1, M+1):
        for value in table[i]:
            heapq.heappush(candidate, value)
        if len(candidate) > 0:
            ret -= heapq.heappop(candidate)

    print(ret)
    
if __name__=="__main__":
    main()
