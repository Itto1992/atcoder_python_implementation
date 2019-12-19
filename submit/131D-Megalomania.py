# import bisect
# import heapq
# import math
# import queue
import sys


def main():
    # 読み込み回数が多い場合
    input = sys.stdin.readline
    N = int(input())
    
    # heap queue
    h = []
    for i in range(N):
        A, B = map(int, input().split())
        h.append((B, A))
    h.sort()
	
    time = 0
    for B, A in h:
        time += A
        if B < time:
            print("No")
            sys.exit()
    
    print("Yes")


if __name__ == "__main__":
    main()
