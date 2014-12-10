import sys, os, socket

input_filename = '/Users/gyz/Dropbox/projects/spoj/input.txt'
output_filename = '/Users/gyz/Dropbox/projects/spoj/output.txt'
local_machine_indicator = 'gyz-mba'

def isRunningOnLocal():
  return local_machine_indicator in socket.gethostname() 

def getIOfiles():
  if isRunningOnLocal():
    return open(input_filename, 'r'), sys.stdout 
  else:
    return sys.stdin, sys.stdout

class TestCase(object):
  def __init__(self, n, k, input_array):
    self.array_length = n
    self.num_of_flip = k
    self.input_array = input_array
    assert len(input_array) == n

  def getResult(self):
    negative_part = [x for x in self.input_array if x < 0]
    negative_part.sort()
    non_negative_part = [x for x in self.input_array if x >= 0]
    if len(negative_part) >= self.num_of_flip:
      return sum(non_negative_part) - sum(negative_part[:self.num_of_flip]) \
        + sum(negative_part[self.num_of_flip:])
    abs_array = [abs(x) for x in self.input_array]
    min_abs = min(abs_array)
    remain_flip = self.num_of_flip - len(negative_part)
    return sum(abs_array) - 2 * (remain_flip % 2) * min_abs

def getTestCaseInputs(input_file):
  raw_input = input_file.readlines()
  total_testcase = int(raw_input[0])
  line_number = 1
  total_input_lines = len(raw_input)
  test_case_inputs = []
  for _ in xrange(total_testcase):
    array_length, num_of_flip = map(int, raw_input[line_number].split())
    line_number += 1
    input_array = map(int, raw_input[line_number].split())
    test_case_inputs.append(TestCase(array_length, num_of_flip, input_array))
    line_number += 1
  return test_case_inputs

def writeToFile(outputs, output_file):
  output_file.write('\n'.join(map(str, outputs)))

def main(): 
  input_file, output_file = getIOfiles()
  raw_testcase_inputs = getTestCaseInputs(input_file) 
  outputs = map(lambda(x): x.getResult(), raw_testcase_inputs)
  writeToFile(outputs, output_file)

if __name__ == '__main__':
  main()
