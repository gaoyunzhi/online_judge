# https://vijos.org/p/1039
from collections import Counter

class Solver():
  def __init__(self):
    self._cache = {}

  def solve(self, occurrence, length):
    if length % 2 == 1:
      return abs(*self.parts(occurence, length))

  def solveRem(self, numbers):
    occurrence = [0] * 10
    for number in numbers:
      occurrence[number] += 1
    occurrence = tuple(occurrence)
    if not occurrence in self._cache:
      self._cache[occurrence] = self.solve(occurrence, len(numbers))
    return self._cache[occurrence]
 

  def parts(self, occurence, length):
    if length == 0:
      return 0, 0
    numbers = list(occurrence)
    asc_part = 0
    if length % 2 == 1:
      min_num = self.findMin(occurence)
      numbers[min_num] -= 1
      asc_part = min_num
    cur_num = 0
    for _ in xrange(length / 2):
      if occurence[cur_num]


  def findMin(self, occurence):
    for i in xrange(1, 10):
      if occurence[i] > 0:
        return i

def main():
  #  handle=sys.stdin
  handle = open("1039.txt", "r") 
  num_case = int(handle.readline())
  solver = Solver()
  for _ in xrange(num_case):
    num = int(handle.readline())
    numbers = map(int, split(handle.readline()))
    solver.solveRem(numbers)
   
if __name__ == '__main__':
  main()