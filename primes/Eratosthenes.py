import math


def primesTo(upTo):
    knownPrimes = [2]
    # to offset lists starting at 0
    upTo += 1
    square_of_upTo = math.sqrt(upTo)
    unknownPrimes = [number for number in xrange(3, upTo, 2)]
    for position, posiblePrime in enumerate(unknownPrimes):
        if posiblePrime and posiblePrime <= square_of_upTo:
            for nonPrime in xrange(position+posiblePrime, len(unknownPrimes), posiblePrime):
                unknownPrimes[nonPrime] = None

    return knownPrimes + [prime for prime in unknownPrimes if prime]