# https://vijos.org/p/1039
from collections import Counter

class Solver():
  def __init__(self):
    self._cache = {}

  def solve(self, occurrence, length):
    if length % 2 == 1:
      return abs(*self.parts(occurrence, length))

  def solveRem(self, numbers):
    occurrence = [0] * 10
    for number in numbers:
      occurrence[number] += 1
    occurrence_string = []
    for i in xrange(10):
      occurrence_string.append(str(i) * occurrence)
    if not occurrence in self._cache:
      self._cache[occurrence] = self.solve(occurrence, len(numbers))
    return self._cache[occurrence]
 

  def parts(self, occurrence, length):
    if length == 0:
      return 0, 0
    numbers = list(occurrence)
    asc_part = 0
    if length % 2 == 1:
      min_num = self.findMin(occurrence)
      numbers[min_num] -= 1
      asc_part = min_num
    cur_num = 0
    for _ in xrange(length / 2):
      if occurrence[cur_num]


  def findMin(self, occurrence):
    for i in xrange(1, 10):
      if occurrence[i] > 0:
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