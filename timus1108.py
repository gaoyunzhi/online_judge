# http://acm.timus.ru/problem.aspx?space=1&num=1025
import sys

def main():
  #  handle=sys.stdin
  handle = open("1108", "r") 
  n = int(handle.readline())
  number = 2
  print 2
  for _ in xrange(n - 1):
    number = number * (number - 1) + 1
    print number


if __name__ == '__main__':
  main()