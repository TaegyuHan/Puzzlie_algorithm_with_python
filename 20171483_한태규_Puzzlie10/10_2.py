def rFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        y = rFib(n - 1) + rFib(n - 2)
    return y

if __name__ == '__main__':
    print(rFib(10))