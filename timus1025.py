# http://acm.timus.ru/problem.aspx?space=1&num=1025
import sys

def main():
  #  handle=sys.stdin
  handle = open("1025", "r") 
  k = int(handle.readline())
  numbers = map(int, handle.readline().split())
  numbers.sort()
  print sum([number / 2 + 1 for number in numbers[: k / 2 + 1]])

if __name__ == '__main__':
  main()