import sys
import queue


# accepted with pypy3
def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())

    edges = {i : [] for i in range(1, N+1)}
    for i in range(N-1):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    
    values = {i : 0 for i in range(1, N+1)}
    for i in range(Q):
        p, x = map(int, input().split())
        values[p] += x
    
    has_noparent = {i : True for i in range(1, N+1)}
    has_noparent[1] = False
    
    q = queue.Queue()
    q.put(1)
    
    while not q.empty():
        parent = q.get()
        value_parent = values[parent]
        for child in edges[parent]:
            if has_noparent[child]:
                values[child] += value_parent
                q.put(child)
                has_noparent[child] = False

    ret = [str(i) for i in values.values()]
    ret = ' '.join(ret)
    print(ret)
    
if __name__=="__main__":
    main()
