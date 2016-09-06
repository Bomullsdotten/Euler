import math

def fibonacci(number):
    golden_ration = (1 + math.sqrt(5)) / 2.0
    return round(math.pow(golden_ration, number)/math.sqrt(5))

def is_even(number):
    if number % 2 == 0:
        return True
    return False


if __name__ == '__main__':
    a = []
    print sum([fibonacci(n) for n in xrange(2,100) if is_even(fibonacci(n)) and fibonacci(n)<4000000])

