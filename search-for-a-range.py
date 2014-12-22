# https://oj.leetcode.com/problems/search-for-a-range/

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
      n = len(A)
      low = 0
      high = n - 1
      while low < high:
        mid = (low + high) / 2
        if A[mid] >= target:
          high = mid
        else:
          low = mid + 1
      start = low
      low = 0
      high = n - 1
      while low < high:
        mid = (low + high + 1) / 2
        if A[mid] > target:
          high = mid - 1
        else:
          low = mid
      end = low
      if A[start] == A[end] and A[end] == target:
        return [start, end]
      return [-1, -1]

def test():
  test_data = [[[[5, 7, 7, 8, 8, 10], 8], [3, 4]]]
  for arg, ans in test_data:
    if Solution().searchRange(*arg) != ans:
      print arg, ans, Solution().searchRange(*arg)
  

if __name__ == '__main__':
  test()
