# https://www.hackerrank.com/challenges/similarpair
import sys, bisect

class Solve():
  def __init__(self, n, t, edges):
    self._n = n
    self._t = t
    self._parent = {}
    self._children = {}
    for parent, child in edges:
      self._parent[child] = parent
      if (not parent in self._children): self._children[parent] = []
      self._children[parent].append(child)
    root = child
    while root in self._parent:
      root = self._parent[root]
    self._root = root

  def solve(self):
    if self._t == 0:
      return 0
    self._ranges = {}
    self._ranges[self.root] = []
    stack = [root]
    pointer = 0
    while pointer <= len(stack):
      node = stack[pointer]
      if node in self._children:
        stack += self._children[node]
      if pointer == 0:
        pointer += 1
        continue
      parent = self._parent[node]
      self._ranges[node] = self._ranges[parent][:]
      index = bisect.bisect_left(self._ranges[node])
      if self._ranges[node][index] + self._t + 1 < parent and \
        (index == len(self._ranges[node] or \
          parent + self._t + 1 < self._ranges[node][index + 1]):
        bisect.insort(self._ranges[node], parent)
      index = bisect.bisect_left(self._ranges[node])

      pointer += 1



def main():
  #  handle=sys.stdin
  handle = open("similarpair.txt", "r") 
  n, t = map(int, handle.readline().split())
  edges = [map(int, handle.readline().split()) for _ in xrange(n - 1)]
  sol = Solve(n, t, edges)
  sys.stdout.write(sol.solve())
  
if __name__ == '__main__':
  main()

'''
tests:
5 2
3 2
3 1
1 4
1 5

'''