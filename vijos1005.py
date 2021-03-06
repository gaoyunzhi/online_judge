# https://vijos.org/p/1039
# test cases http://acm.timus.ru/forum/?space=1&num=1165
import sys, random

class Solver():
  def __init__(self, string):
    self._string = string
    self.len = len(self._string)
    self.initMin()
    self.updateEasyCaseMin() #  where start can be extraced
    self.updateHardCaseMin() #  where start can not be extraced

  def getAns(self):
    digit = len(str(self.min))
    ans = 0
    for i in xrange(1, digit):
      ans += 9 * i * 10 ** (i - 1) 
    ans += digit * (self.min - 10 ** (digit - 1))  
    ans -= self.pos
    return ans + 1

  def initMin(self):
    if self._string[0] == '0':
      self.min = int('1' + self._string) + 1
      self.pos = self.len
    else:
      self.min = int(self._string)
      self.pos = 0

  def updateEasyCaseMin(self):
    for start_ind in xrange(self.len):
      if self._string[start_ind] == '0': 
        continue
      for end_ind in xrange(start_ind * 2, self.len):
        start = self._string[start_ind: end_ind + 1]
        start_int = int(start)
        if start_int > self.min or (start_int == 1 and start_ind != 0): 
          continue
        potential_list = map(
          str, 
          range(start_int - 1, start_int + self.len / len(start) + 1)
        )
        potential_string = ''.join(potential_list)
        if not potential_string[len(potential_list[0]) - start_ind:] \
          .startswith(self._string):
          continue
        self._updateMin(start_int, start_ind)

  def updateHardCaseMin(self):
    for start_ind in xrange(1, self.len):
      second_part = self._string[start_ind:]
      if second_part[0] == '0': 
        continue
      first_part = self._string[:start_ind]
      second_part_int = int(second_part)
      if second_part_int > self.min:
        continue
      for num in xrange(1, start_ind + 1):
        tail = first_part[start_ind - num:]
        if tail == '9' * num and second_part_int > 1 \
          and str(second_part_int - 1).endswith(first_part[:start_ind - num]):
          self._updateMin(int(str(second_part_int - 1) + tail) + 1, start_ind)
        if tail != '9' * num and second_part.endswith(first_part[:start_ind - num]):
          self._updateMin(int(second_part + tail) + 1, start_ind)

  def _updateMin(self, new_min, pos):
    if new_min == self.min:
      self.pos = max(self.pos, pos)
      return
    if new_min < self.min:
      self.min = new_min
      self.pos = pos          

def main():
  #  handle=sys.stdin
  handle = open("1005.txt", "r") 
  string = handle.readline().strip()
  sol = Solver(string)
  sys.stdout.write(str(sol.getAns()))
   
def test():
  string = ''.join(map(str, xrange(1, 100000)))
  print Solver('2020').getAns() == 6970
  print Solver('999').getAns() == 2588
  print Solver(string[:100]).getAns() == 1
  print Solver('1').getAns() == 1
  print Solver('5').getAns() == 5
  print Solver('101').getAns() == 10
  print Solver('01').getAns() == 11
  print Solver('1011').getAns() == 10
  print Solver('12345').getAns() == 1
  print Solver('012345').getAns() == 629595
  print Solver('9920').getAns() == 488
  print Solver('0112').getAns() == 3373

  for i in xrange(2000):
    if random.random() > 0.005: continue
    for j in xrange(i, 2000):
      if random.random() > 0.005: continue
      substring = string[i: j + 1]
      ind = string.find(substring)
      if Solver(substring).getAns() != ind + 1:
        print '- attention -'
        print i, j
        print substring, Solver(substring).getAns()

if __name__ == '__main__':
  # main()
  test()