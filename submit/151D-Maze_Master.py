import bisect
import math
import sys
from collections import Counter, defaultdict, deque
from copy import copy, deepcopy
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations
from queue import Queue

read = sys.stdin.read
readline = sys.stdin.readline 
readlines = sys.stdin.readlines 

inf = float("inf")


def main():

    H, W = map(int, readline().split())
    S = [[s for s in input()] for h in range(H)]
    
    ret = 0
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                tmp_ret = 0
                maze = deepcopy(S)
                maze[h][w] = tmp_ret
                
                q1 = Queue()
                q1.put((h, w))
                
                q2 = Queue()
                
                while not (q1.empty() and q2.empty()):
                    while not q1.empty():
                        h, w = q1.get()
                        for dh, dw in delta:
                            if h + dh < H and h + dh >= 0 \
                            and w + dw < W and w + dw >= 0 \
                            and maze[h + dh][w + dw] == '.':
                                maze[h + dh][w + dw] = '#'
                                q2.put((h + dh, w + dw))

                    if not q2.empty():
                        q1 = q2
                        q2 = Queue()
                        tmp_ret += 1
                        
                ret = max(ret, tmp_ret)
    
    print(ret)


if __name__ == "__main__":
    main()
