import math
def primesTo(upTo):
    # to offset lists starting at 0
    upTo += 1

    primes = [True]*upTo
    primes[0] = False
    primes[1] = False
    for number in xrange(2, int(math.sqrt(upTo))+1):
        if primes[number]:
            for nonPrime in xrange(number*2, upTo, number):
                primes[nonPrime] = False

    return [position for position, value in enumerate(primes) if value]




if __name__ == '__main__':
    pass