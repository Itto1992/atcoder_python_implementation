import sys, heapq


def main():
    # ノートブック上では動かない atcoder上ではこちらが動きかつ高速
    # input = sys.stdin.readline
    
    N, M = map(int, input().split())
    value = [-int(inp) for inp in input().split()]

    heapq.heapify(value)

    for _ in range(M):
        new_elem = -(- heapq.heappop(value) // 2)
        heapq.heappush(value, new_elem)

    print(- sum(value))
    
if __name__=="__main__":
    main()
