#!/usr/bin/python3
# coding: utf-8

import sys, math


def pow(a, k, n):
    result = 1
    while k != 0:
        if k & 1 != 0:
            result = (result * a) % n
        a = (a * a) % n
        k = k // 2
    return result


def is_prime_naive(n):
    a = 2
    while a * a <= n:
        if n % a == 0:
            return False
        a += 1
    return True


def pow2_in_n(n):
    result = 0
    while n != 0 and n % 2 == 0:
        result += 1
        n = n // 2
    return result


def is_prime_rabin_miller_base(a, n):
    k = pow2_in_n(n - 1)
    q = (n - 1) // (2 ** k)
    r = pow(a, q, n)
    if r == 1 or r == n - 1:
        return True
    while k != 0:
        r = (r * r) % n
        if r == n - 1:
            return True
        k -= 1
    return False


def is_prime_rabin_miller(n):
    for a in range(2, min(70 * int(math.log(n) / math.log(2) + 1), n)):
        if not is_prime_rabin_miller_base(a, n):
            return False
    return True


def is_prime(n):
    return is_prime_rabin_miller(n) if n >= 30000 else is_prime_naive(n)


def test():
    for a in range(3, 10000):
        if is_prime_naive(a) != is_prime_rabin_miller(a):
            print('Wrong answer: {}'.format(a))
            return False
    print('Test OK')
    return True


def check_and_print(n):
    print('{}: {}'.format(n, is_prime(n)))


def main():
    test()
    check_and_print(12345678910987654321)
    check_and_print(1000000000000066600000000000001)
    check_and_print(12345678910987654321 + 12)
    check_and_print(1000000000000066600000000000001 + 12)
    check_and_print(2**521-1)

if __name__ == "__main__":
    main()

