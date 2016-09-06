
def multiple_of_x(numerator, denominator):
    if numerator % denominator == 0:
        return True
    return False


def multiples_in_range(range_, *denominators):
    result = set()

    for number in xrange(1, range_):
        for denom_ in denominators:
            if multiple_of_x(number, denom_):
                result.add(number)
    return sorted(list(result))


def sum_multiples_in_range(range_, *denominators):
    return sum(multiples_in_range(range_, *denominators))


if __name__ == '__main__':
    print sum_multiples_in_range(1000, 3, 5)


