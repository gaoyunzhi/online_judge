import sys, os, socket

input_filename = '/Users/gyz/Dropbox/projects/spoj/input.txt'
output_filename = '/Users/gyz/Dropbox/projects/spoj/output.txt'
local_machine_indicator = 'gyz-mba.dhcp'
shape = {1: '/', -1: '\\', 0: '_'}

def isRunningOnLocal():
 return local_machine_indicator in socket.gethostname() 

def getIOfiles():
  if isRunningOnLocal():
    return open(input_filename, 'r'), sys.stdout 
  else:
    return sys.stdin, sys.stdout

def getTestCaseInputs(input_file):
  raw_input = input_file.readlines()
  line_number = 0
  total_input_lines = len(raw_input)
  test_case_inputs = []
  while line_number < total_input_lines:
    num_of_col = int(raw_input[line_number])
    if num_of_col == -1:
      break
    line_number += 1
    raw_skyline = map(int, raw_input[line_number].split())
    assert len(raw_skyline) == num_of_col + 1
    test_case_inputs.append(raw_skyline)
    line_number += 1
  return test_case_inputs

def formatSkyline(testcase_input):
  formatted_line_map = {}
  num_of_col = len(testcase_input) -1
  for col_num in xrange(num_of_col):
    current_height = testcase_input[col_num+1]
    previous_height = testcase_input[col_num]
    output_height = (current_height + previous_height) / 2
    output_shape = shape[current_height - previous_height]
    if not output_height in formatted_line_map:
      formatted_line_map[output_height] = []
    formatted_line_map[output_height].append((col_num, output_shape))
  return formatted_line_map

def skylineToString(skyline):
  heights = skyline.keys()
  min_height = min(heights)
  max_height = max(heights)
  output = []
  for height in xrange(max_height, min_height-1, -1):
    shape_on_height = skyline[height]
    last_col = -1
    for col, shape in shape_on_height:
      output.append(' ' * (col - last_col -1) + shape)
      last_col = col
    output.append('\n')
  output.append('***\n')
  return ''.join(output)

def writeToFile(outputs, output_file):
  output_file.write(''.join(outputs))

def main(): 
  input_file, output_file = getIOfiles()
  raw_testcase_inputs = getTestCaseInputs(input_file) 
  outputs = map(formatSkyline, raw_testcase_inputs)
  outputs = map(skylineToString, outputs)
  writeToFile(outputs, output_file)

if __name__ == '__main__':
  main()
