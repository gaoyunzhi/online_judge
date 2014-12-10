# https://vijos.org/p/1039
import sys

class Solver():
  def __init__(self):
    self._cache = {}

  def solve(self, occurrence, occurrence_string):
    if len(occurrence_string) % 2 == 1:
      return self._partsDifference(occurrence_string)
    multiplier = 10 ** (len(occurrence_string) / 2 - 1)
    cur_min = int(occurrence_string)
    for top_difference in xrange(1, 10):
      if (top_difference - 1) * multiplier > cur_min:
        break
      for top_first in xrange(1, 10 - top_difference):
        top_second = top_first + top_difference
        if not occurrence[top_second] or not occurrence[top_first]: 
          continue
        modified_string = \
          occurrence_string.replace(str(top_first), '', 1) \
          .replace(str(top_second), '', 1)
        cur_difference = \
          self._partsDifference(modified_string) + top_difference * multiplier
        print cur_difference, modified_string
        cur_min = min(cur_difference, cur_min)
    for top in xrange(1, 10):
      if occurrence[top] >= 2:
        for num_tail_zero in xrange(occurrence[0] / 2 + 1):
          modified_string = \
            occurrence_string.replace(str(top), '', 2) \
            .replace('0', '', num_tail_zero * 2)
          modified_occurrence = occurrence[:]
          modified_occurrence[0] -= num_tail_zero * 2
          modified_occurrence[top] -= 2
          cur_difference = self.solveRemInternal(modified_occurrence, occurrence_string)    
          cur_min = min(cur_difference, cur_min)
    return cur_min

  def solveRemInternal(self, occurrence, occurrence_string):
    if not occurrence_string in self._cache:
      self._cache[occurrence_string] = self.solve(occurrence, occurrence_string)
    return self._cache[occurrence_string]

  def solveRem(self, numbers):
    occurrence = [0] * 10
    for number in numbers:
      occurrence[number] += 1
    occurrence_string = []
    for i in xrange(10):
      occurrence_string.append(str(i) * occurrence[i])
    occurrence_string = ''.join(occurrence_string)
    if not occurrence_string in self._cache:
      self._cache[occurrence_string] = self.solve(occurrence, occurrence_string)
    return self._cache[occurrence_string]

  def _partsDifference(self, occurrence):
    if len(occurrence) == 0:
      return 0
    occurrence_modified = occurrence
    if len(occurrence) % 2 == 1:
      for index, number in enumerate(occurrence):
        if number != '0':
          occurrence_modified = number + occurrence[:index] + occurrence[index + 1:]
          break
    return int(occurrence_modified[: (len(occurrence) + 1) / 2]) - \
      int(occurrence_modified[(len(occurrence) + 1) / 2 :][:: -1])

def main():
  #  handle=sys.stdin
  handle = open("1039_2.txt", "r") 
  num_case = int(handle.readline())
  solver = Solver()
  ans = []
  for _ in xrange(num_case):
    num = int(handle.readline())
    numbers = map(int, handle.readline().split())
    ans.append(solver.solveRem(numbers))
  sys.stdout.write('\n'.join(map(str, ans)))
   
if __name__ == '__main__':
  main()