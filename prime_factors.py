#!/usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math as m

def is_prime(n):
    for x in xrange(2, int(m.sqrt(n))+1):
        if (n % x == 0):
            return False
    return True


def prime_factors(n):
    for x in xrange(2, int(n/2)):
        if (n % x == 0 and is_prime(x)):
            yield x

while True:
    try:
        n = int(raw_input('Find prime factors of: '))
        for x in prime_factors(n):
            print x
    except ValueError:
        print 'Must enter integer'

