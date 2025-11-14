def fibo():
    pad = {0: 0, 1: 1}
    def fibo_inner(n):
        if not n in pad:
            pad[n] = fibo_inner(n - 1) + fibo_inner(n - 2)
        return pad[n]
    return fibo_inner
if __name__ == '__main__':
    func = fibo()
    print(func(6))
