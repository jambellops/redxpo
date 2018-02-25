def genPrime():
    yield 2
    primeSeq = [2]
    prim_test = 3
    while True:
        next = prim_test
        test_flag = False
        # x is prime if (x % p) != 0 for all earlier primes p
        for p in primeSeq:
            if prim_test % p == 0:
                test_flag = False
                break
            elif prim_test % p != 0:
                test_flag = True
        if test_flag == True:
            primeSeq.append(prim_test)
            yield next
        else:
            pass
        prim_test += 1
