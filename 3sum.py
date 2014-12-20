# https://oj.leetcode.com/problems/3sum/

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
      return list(self.threeSumInternal(num))

    def threeSumInternal(self, num):
        n = len(num)
        num.sort()
        counter = {}
        for x in num:
          if not x in counter: 
            counter[x] = 0
          counter[x] += 1
        last = [-float('Inf'), -float('Inf')]
        for first_ind, first_num in enumerate(num):
          for second_ind in xrange(first_ind + 1, n):
            second_num = num[second_ind]
            if [first_num, second_num] < last:
              break
            if [first_num, second_num] == last:
              continue
            third_num = -first_num - second_num
            if third_num < second_num:
              last = [first_num, second_num]
              break
            potential_ans = [first_num, second_num, third_num]
            occurrence = potential_ans.count(third_num)
            if (not third_num in counter) or counter[third_num] < potential_ans.count(third_num):
              last = [first_num, second_num]
              continue
            last = [first_num, second_num]
            yield potential_ans

        

def test():
  test_data = [[[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]]]
  for arg, ans in test_data:
    if list(Solution().threeSum(arg)) != ans:
      print arg, ans, list(Solution().threeSum(arg))
  

if __name__ == '__main__':
  test()