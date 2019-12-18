# import bisect
# import heapq
# import math
# import queue
import sys


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    a = {i: inp for i, inp in enumerate(map(int, input().split()))}
    
    partial_sum = 0
    ret = 0
    start = 0
    for i in range(N):
        partial_sum += a[i]
        if partial_sum >= K:
            ret += N - i
            while partial_sum >= K and start <= i:
                partial_sum -= a[start]
                start += 1
                if partial_sum >= K:
                    ret += N - i
                    
    print(ret)
    
    
if __name__=="__main__":
    main()
