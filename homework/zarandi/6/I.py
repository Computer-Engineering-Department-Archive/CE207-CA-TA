for n in range(1, 32):
    for k in range(1, 32):
        if k*(n+4) + n == 32:
            print("n >> " + str(n) + " k >> " + str(k))
            delay = 8*k + 8*n*k + 8*n
            print('delay >> ' + str(delay) + '\n')