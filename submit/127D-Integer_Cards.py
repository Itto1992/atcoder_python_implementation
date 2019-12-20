import sys
from collections import defaultdict


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    A = defaultdict(int)
    for i in map(int, input().split()):
        A[i] += 1
        
    for i in range(M):
        B, C = map(int, input().split())
        A[C] += B
        
    ret = 0
    count = 0
    for value, num_value in sorted(A.items(), key=lambda x:x[0])[::-1]:
        num_value = min(num_value, N - count)
        ret += value * num_value
        count += num_value
        if num_value == N:
            break
    
    print(ret)


if __name__ == "__main__":
    main()
