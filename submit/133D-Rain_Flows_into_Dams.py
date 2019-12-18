def main():
    N = int(input())
    A = {i:inp for i, inp in enumerate(map(int, input().split()), 1)}

    for i in range(2, N+1):
        A[i] -= A[i - 1]
    
    const = A[N] // 2
    ret = [str(2 * const)]

    for i in range(1, N):
        if i % 2:
            ret.append(str(2 * (A[i] - const)))
        else:
            ret.append(str(2 * (A[i] + const)))

    ret = ' '.join(ret)
    print(ret)
    

if __name__=="__main__":
    main()
