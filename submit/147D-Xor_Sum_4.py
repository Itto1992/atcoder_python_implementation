N = int(input())
binary = [0]*60
for inp in input().split():
    inp = bin(int(inp))[2:][::-1]
    for j, _inp in enumerate(inp):
        if _inp == '1':
            binary[j] += 1
    
ret = 0
pow2 = 1
for elem in binary:
    if elem == 0 or elem == N:
        pass
    else: 
        mn = elem * (N - elem) % (10**9 + 7)
        ret += pow2 * mn 
        ret = ret % (10**9 + 7)
    pow2 = pow2 * 2 % (10**9 + 7)
print(ret)

