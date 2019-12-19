def main():
    S = {i:s for i, s in enumerate(input()[::-1])}
    MOD = 10**9 + 7

    DP_table = [[0 for i in range(13)] for j in range(len(S))]
    
    digit = S[0]
    if digit == '?':
        for i in range(10):
            DP_table[0][i] = 1
    else:
        DP_table[0][int(digit)] = 1
    
    multiplier = 1
    for i in range(1, len(S)):
        digit = S[i]
        multiplier = multiplier * 10 % 13
        if digit == '?':
            for j in range(10):
                for k in range(13):
                    DP_table[i][(j * multiplier + k) % 13] += DP_table[i-1][k]
        else:
            digit = int(digit)
            for k in range(13):
                DP_table[i][(digit * multiplier + k) % 13] += DP_table[i-1][k]
        
        for j in range(13):
            DP_table[i][j] %= MOD

    print(DP_table[len(S)-1][5])

    
if __name__ == "__main__":
    main()
