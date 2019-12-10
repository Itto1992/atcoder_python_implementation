N = int(input())
L = [i for i in map(int, input().split())]

L = sorted(L)[::-1] # descending order

def binary_search(descend_list, threshold):
    # 閾値を超えている要素の数を返す
    length = len(descend_list)
    
    # 最小の数が閾値を超えればリストの長さを返す
    if descend_list[-1] > threshold:
        return length
    
    # 最大の数が閾値を超えなければ0を返す
    if descend_list[0] <= threshold:
        return 0
    
    # 二分探索する 少なくとも一つはthresholdを超える要素があり、少なくとも一つはthresholdを超えない要素がある場合
    upper_bound = length
    lower_bound = 0
    index = (upper_bound - lower_bound) // 2
    
    while upper_bound > lower_bound + 1:
        if descend_list[index] > threshold:
            lower_bound = index
        else:
            upper_bound = index
        
        index = (upper_bound + lower_bound) // 2
    
    return lower_bound + 1

i = 0
ret = 0

while i < N - 2:
    edge1 = L[i]
    for j in range(i + 1, N-1):
        edge2 = L[j]
        _ret = binary_search(L[j+1:], edge1 - edge2)
        if _ret == 0:
            break
        else:
            ret += _ret
    
    i += 1

print(ret)

