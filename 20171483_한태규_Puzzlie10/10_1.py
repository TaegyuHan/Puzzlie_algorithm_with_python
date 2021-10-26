def iGcd(m, n):
    while n > 0:
        m, n = m % n
    return m

def rGcd(m, n):
    print(m, n)
    if m & n == 0:
        return n
    else:
        gcd = rGcd(n, m % n)
        return gcd

if __name__ == '__main__':
    rGcd(2002, 1344)