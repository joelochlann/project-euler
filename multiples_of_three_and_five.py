#!/usr/bin/env python

# If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Think this has O(limit) complexity because count
# is proportional to limit (given constant n).
# So the range of numbers we have to sum increases
# linearly with limit.
# Could probably do better!
# Perhaps by considering the formula for the sum or an arithmetic series?
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

