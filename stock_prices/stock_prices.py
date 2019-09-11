#!/usr/bin/python

import argparse

p = [10, 7, 5, 8, 11, 9]
p2 = [100, 90, 80, 50, 20, 10]

def find_max_profit(prices):
    largest_gain = prices[1] - prices[0]
    for i in range(len(prices) - 2):
      for j in range(i + 1, len(prices) - 1):
        if prices[j] - prices[i] > largest_gain:
          largest_gain = prices[j] - prices[i]

    return largest_gain


print(find_max_profit(p2))

if __name__ == '__main__':
  pass
  This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))