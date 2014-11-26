#!/usr/bin/env python

def sum_of_multiples(n, limit):
   r = (limit - 1) % n
   count = (limit - r) / n
   return (n * sum(range(1, count + 1)))

while True:
  try:
    lim = int(raw_input("Sum of multiples of five and three below: "))
    print (sum_of_multiples(5, lim) + sum_of_multiples(3, lim)) - sum_of_multiples(15, lim)
    break
  except ValueError:
    print "Must enter an integer"

