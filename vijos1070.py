# https://vijos.org/p/1070
import sys

class Node():
  def __init__(self, key):
    self.key = key
    self.root = self
    self.rank = 0

  def setParent(self, new_parent):
    self.root = new_parent
    self.rank = new_parent.rank + 1

  def findRoot(self):
    if self.root == self:
      return self
    self.root = self.root.findRoot()
    return self.root

  def getRank(self):
    return self.rank

class Solve():
  def __init__(self, n, edges):
    self.edges = edges
    self.nodes = [Node(x) for x in xrange(n)]
    self.mstEdgeInd = set()
    self.calulateMST()
    self.calulateSecondMst()

  def calulateMST(self):
    self.mstTotal = 0
    self.mst_node_map = [[]] * len(self.nodes)
    for index, (i, j, cost) in enumerate(self.edges):
      rootA, rootB = self.nodes[i].findRoot(), self.nodes[j].findRoot()
      if rootA == rootB:
        continue
      self.mstEdgeInd.add(index)
      self.mstTotal += cost
      if rootB.getRank() > rootA.getRank():
        rootA, rootB, = rootB, rootA
      rootA.setParent(rootB)
      self.mst_node_map[i].append(j)
      self.mst_node_map[j].append(i)
    roots = map(lambda node: node.findRoot(), self.nodes)
    if not (roots == [roots[0]] * len(roots)):
      self.mstTotal = -1
      return

  def findPartition(self, u, v):
    self.partition.add(u)
    for new_node in self.mst_node_map[u]:
      if new_node == v or new_node in self.partition:
        continue
      self.findPartition(new_node, v)

  def calulateSecondMst(self):
    if self.mstTotal == -1:
      self.secondMSTCost = -1
      return
    self.secondMSTCost = float('Inf')
    for index_uv in self.mstEdgeInd:
      u, v, cost_uv = self.edges[index_uv]
      self.partition = set()
      self.findPartition(u, v)
      for index_ij, (i, j, cost_ij) in enumerate(self.edges):
        if index_ij in self.mstEdgeInd: continue
        if (i in self.partition) ^ (j in self.partition): 
          self.secondMSTCost = \
            min(self.secondMSTCost, self.mstTotal - cost_uv + cost_ij)
          break
    if self.secondMSTCost == float('Inf'):
      self.secondMSTCost = -1

  def getAns(self):
    return 'Cost: ' + str(self.mstTotal) + '\nCost: ' + str(self.secondMSTCost)

def main():
  #  handle=sys.stdin
  handle = open("1070.txt", "r") 
  n, m = map(int, handle.readline().split())
  edges = [map(int, handle.readline().split()) for _ in xrange(m)]
  edges = map(lambda (i, j ,c): (i - 1, j - 1, c), edges)
  edges = sorted(edges, key=lambda edge: edge[2])
  sol = Solve(n, edges)
  sys.stdout.write(sol.getAns())
  
if __name__ == '__main__':
  main()

'''
tests:
4 6
1 2 2
2 3 2
3 4 4
4 1 2
1 3 1
2 4 4

'''