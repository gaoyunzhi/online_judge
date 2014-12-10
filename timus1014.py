# https://vijos.org/p/1070
import sys

class Sol():
  def __init__(self, n):
    self.n = n

  def getAns(self):
    if self.n == 0:
      return '10'
    if self.n == 1:
      return '1'
    power = [0] * 10
    m = self.n
    for key in [2, 3, 5, 7]:
      while m % key == 0:
        m /= key
        power[key] += 1
    if m > 1:
      return '-1'
    power[9] = power[3] / 2
    power[3] = power[3] % 2
    power[8] = power[2] / 3
    power[2] = power[2] % 3
    if power[3] and power[2]:
      power[6] = 1
      power[3] -= 1
      power[2] -=1
    power[4] = power[2] / 2
    power[2] = power[2] % 2

    ans = [str(key) * power[key] for key in xrange(10)]
    return ''.join(ans)

def main():
  #  handle=sys.stdin
  handle = open("1014", "r") 
  n = int(handle.readline())
  sys.stdout.write(Sol(n).getAns())

def test():
  print Sol(0).getAns() == '10'
  print Sol(1).getAns() == '1'
  print Sol(2).getAns() == '2'
  print Sol(4).getAns() == '4'
  print Sol(14).getAns() == '27'
  print Sol(28).getAns() == '47'
  print Sol(56).getAns() == '78'
  print Sol(27).getAns() == '39'
  print Sol(6).getAns() == '6'
  print Sol(11).getAns() == '-1'
  print Sol(24).getAns() == '38'
  print Sol(12).getAns() == '26'

if __name__ == '__main__':
  # main()
  test()
