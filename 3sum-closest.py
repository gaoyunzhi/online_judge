class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        n = len(num)
        ans = sum(num[:3])
        for first_ind, first_num in enumerate(num):
          third_ind = n - 1
          second_ind = first_ind + 1
          while second_ind < third_ind:
            cur_ans = num[second_ind] + num[third_ind] + first_num
            if abs(cur_ans - target) < abs(ans - target):
              ans = cur_ans
            if cur_ans > target:
              third_ind -= 1
            else:
              second_ind += 1
        return ans

def test():
  test_data = [[[[-1, 2, 1, -4], 1], 2]]
  for arg, ans in test_data:
    if Solution().threeSumClosest(*arg) != ans:
      print arg, ans, Solution().threeSumClosest(*arg)
  

if __name__ == '__main__':
  test()
