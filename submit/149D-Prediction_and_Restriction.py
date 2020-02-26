N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

ret = 0
for i in range(K):
    prev = '?'
    for j in range(len(T) // K + 1):
        if i + K*j >= len(T):
            break
        now = T[i + K*j]
        
        if prev == now:
            prev = '?'
        else:
            prev = now
            if now == 'r':  
                ret += P
            elif now == 's':
                ret += R
            else:
                ret += S
            
print(ret)