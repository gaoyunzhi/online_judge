# https://oj.leetcode.com/problems/3sum/

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num_list):
      self.counter = {}
      for x in num_list:
          if not x in self.counter: 
            self.counter[x] = 0
          self.counter[x] += 1
      self.distinctNumList = list(set(num_list))
      self.distinctNumList.sort()
      return list(self.threeSumInternal())

    def threeSumInternal(self):
      n = len(self.distinctNumList)
      for first_ind, first_num in enumerate(self.distinctNumList):
        for second_ind in xrange(first_ind, n):
          second_num = self.distinctNumList[second_ind]
          third_num = - (first_num + second_num)
          if third_num < second_num:
            break
          potential_ans = [first_num, second_num, third_num]
          if potential_ans.count(second_num) > self.getCount(second_num) or \
            potential_ans.count(third_num) > self.getCount(third_num):
            continue
          yield potential_ans

    def getCount(self, x):
      if not x in self.counter:
        return 0
      return self.counter[x]

def test():
  test_data = [
    [[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]], 
    [[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]]
  ]
  for arg, ans in test_data:
    if list(Solution().threeSum(arg)) != ans:
      print arg, ans, list(Solution().threeSum(arg))
  

if __name__ == '__main__':
  test()