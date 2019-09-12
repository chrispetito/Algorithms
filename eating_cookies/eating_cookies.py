#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

cookies = 10

cache = {0: 0, 1: 1}

def eating_cookies(n, cache=None):
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 2
  elif cache is not None and n in cache:
    return cache[n]
  else:
    result = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    if cache is not None:
      cache[n] = result
    return result
  

print(eating_cookies(cookies))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')