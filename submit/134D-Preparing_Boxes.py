def main():

    N = int(input())
    a = {i: inp for i, inp in enumerate(map(int, input().split()), 1)}
        
    b = {i : 0 for i in range(1, N+1)}
    ret = []

    for i in range(N, 0, -1):
        sum_multiple = 0
        cursor = 2
        while i * cursor <= N:
            sum_multiple += b[i * cursor]
            cursor += 1

        if a[i] == 1:
            if sum_multiple % 2 == 0:
                b[i] = 1
                ret.append(i)
        else:
            if sum_multiple % 2:
                b[i] = 1
                ret.append(i)

    M = len(ret)
    print(M)
    if M:
        ret = ' '.join([str(i) for i in ret])
        print(ret)

if __name__=="__main__":
    main()
