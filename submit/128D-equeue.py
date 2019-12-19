import sys


def main():
    # 読み込み回数が多い場合
    input = sys.stdin.readline
    # 複数
    N, K = map(int, input().split())

    # リスト読み込み
    V_A = [inp for inp in map(int, input().split())]
    V_B = V_A.copy()[::-1]
    
    ret = 0
    for A in range(min(K + 1, N + 1)):
        for B in range(min(K - A + 1, N - A + 1)):
            left_jewels = V_A.copy()[:A]
            right_jewels = V_B.copy()[:B]

            if len(left_jewels) >= len(right_jewels):
                jewels = left_jewels
                jewels.extend(right_jewels)
            else:
                jewels = right_jewels
                jewels.extend(left_jewels)
            jewels.sort()

            score = sum(jewels)

            for i in range(min(K - A - B, len(jewels))):
                jewel = jewels[i]
                if jewel < 0:
                    score -= jewel
                else:
                    break
                    
            ret = max(ret, score)
                
    print(ret)

    
if __name__ == "__main__":
    main()
