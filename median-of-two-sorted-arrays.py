import random, bisect

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
      return self.findMedianNSortedArrays(A, B)
        
    def findMedianNSortedArrays(self, *lists):
      n = len(lists)
      left = [0] * n
      right = [len(lst) for lst in lists]
      num_total = sum(right)
      while True:
        num_middle = sum(right[ind] - left[ind] for ind in xrange(n))
        num_min = min([lists[ind][left[ind]] for ind in xrange(n) if left[ind] < right[ind]])
        num_max = max([lists[ind][right[ind] - 1] for ind in xrange(n) if left[ind] < right[ind]])
        if num_min == num_max: 
          if num_total % 2 == 1:
            return num_min
          next = [lists[ind][left[ind]] for ind in xrange(n) if left[ind] < len(lists[ind])]  + \
            [lists[ind][left[ind] + 1] for ind in xrange(n) if left[ind] + 1 < len(lists[ind])]
          next.remove(num_min)
          return (num_min + min(next)) * 0.5
        pivot_rank = random.randint(0, num_middle - 1)
        pivot_ind = -1
        while pivot_rank >= 0:
          pivot_ind += 1
          pivot_rank -= right[pivot_ind] - left[pivot_ind]
        pivot_rank += right[pivot_ind]
        pivot = lists[pivot_ind][pivot_rank]
        mid = [bisect.bisect(lst, pivot) for lst in lists]
        num_left = sum([mid[ind] for ind in xrange(n)])
        if num_left * 2 < num_total:
          left = mid
        else:
          right = mid

def main():
  test_case = [
    [[[1, 3, 5], [2, 4]], 3],
    [[[1,3,5], [2,4,6], [10,20,30], [11,12,23]], 8],
    [[[1,2,3]], 2],
    [[[1,1,1,1]],1],
    [[[1,2,3,4]], 2.5],
  ]
  for args, expected_ans in test_case:
    ans = Solution().findMedianNSortedArrays(*args)
    if ans != expected_ans:
      print args, ans, expected_ans
  
if __name__ == '__main__':
  main()
