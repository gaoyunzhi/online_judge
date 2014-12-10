# https://vijos.org/p/1070
import sys

class Node():
  def __init__(self, key):
    self.key = key
    self.root = self
    self.mstParent = self
    self.rank = 0

  def setParent(self, new_parent):
    self.root = new_parent
    self.mstParent = new_parent
    self.rank = new_parent.rank + 1

  def findRoot(self):
    if self.root == self:
      return self
    self.root = self.root.findRoot()
    return self.root

  def getMstParent(self):
    return self.mstParent

  def getRank(self):
    return self.rank

  def clearRoot(self):
    self.root = self.mstParent

  def setMstParent(self, new_mst_parent):
    self.mstParent = new_mst_parent

class Solve():
  def __init__(self, n, edges):
    self.edges = edges
    self.nodes = [Node(x) for x in xrange(n)]
    self.mstEdgeInd = set()
    self.calulateMst()
    self.calulateSecondMst()

  def calulateMst(self):
    self.mstTotal = 0
    for index, (i, j, cost) in enumerate(self.edges):
      rootA = self.nodes[i].findRoot()
      rootB = self.nodes[j].findRoot()
      if rootA == rootB:
        continue
      self.mstEdgeInd.add(index)
      self.mstTotal += cost
      if rootB.getRank() > rootA.getRank():
        rootA, rootB = rootB, rootA
      rootA.setParent(rootB)
    roots = map(lambda node: node.findRoot(), self.nodes)
    if not (roots == [roots[0]] * len(roots)):
      self.mstTotal = -1

  def calulateSecondMst(self):
    if self.mstTotal == -1:
      self.secondMSTCost = -1
      return
    self.secondMSTCost = float('Inf')
    for index in self.mstEdgeInd:
      u, v, cost_uv = self.edges[index]
      nodeA = self.nodes[u]
      nodeB = self.nodes[v]
      if nodeA.getMstParent() == nodeB:
        nodeA, nodeB = nodeB, nodeA
      nodeB.setMstParent(nodeB)
      map(lambda node: node.clearRoot(), self.nodes)
      for index, (i, j, cost_ij) in enumerate(self.edges):
        if index in self.mstEdgeInd: continue
        rootI = self.nodes[i].findRoot()
        rootJ = self.nodes[j].findRoot()
        if rootI == rootJ: 
          continue
        self.secondMSTCost = \
          min(self.secondMSTCost, self.mstTotal - cost_uv + cost_ij)
        break
      nodeB.setMstParent(nodeA)
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