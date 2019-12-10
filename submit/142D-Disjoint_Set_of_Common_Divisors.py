
def main():
    A, B = map(int, input().split())
    while B!= 0: A, B = B, A % B 
    print(num_prime_factor(A))

def num_prime_factor(n):
    
    if n == 1: return 1
    
    ret = 1
    cursor = 2
    if n % cursor == 0: ret += 1
    while n % cursor == 0: n = n // cursor
    
    cursor = 3
    while cursor**2 <= n:
        if n == 1: return ret
        if n % cursor == 0: ret += 1
        while n % cursor == 0: n = n // cursor
        cursor += 2

    if n != 1: ret += 1
        
    return ret

if __name__ == "__main__":
    main()
