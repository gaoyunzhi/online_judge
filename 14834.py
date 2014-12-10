# Practice disjoint set
# http://www.spoj.com/problems/FOXLINGS/
class DisjointSet():
  def __init__(self, n):
    self.data = [x for x in range(n)]
    self.id = [x for x in range(n)]
    self.num = n # number of disjoint sets
    self.sz = [1 for x in range(n)]
    self.n = n
  def findRoot(self, val):
    while val != self.id[val]:
      self.id[val] = self.id[self.id[val]]
      val = self.id[val]
    return val
  def union(self, val1, val2):
    val1 = self.findRoot(val1)
    val2 = self.findRoot(val2)
    if val1 == val2:
      return
    if self.sz[val1] > self.sz[val2]:
      self.id[val2] = val1
      self.sz[val1] += self.sz[val2]
    else:
      self.id[val1] = val2
      self.sz[val2] += self.sz[val1]
    self.num -= 1

  def find(self, val1, val2):
    val1 = self.findRoot(val1)
    val2 = self.findRoot(val2)
    return val1 == val2

def main():
  #g=sys.stdin
  g = open("FOXLINGS", "r") 
  s=g.read().splitlines()
  while '' in s: s.remove('')
  while '\n' in s: s.remove('\n')

  l1 = s[0].split( )
  num_nodes = int(l1[0])
  num_edges = int(l1[1])
  edges = []
  for edge in range(1, num_edges + 1):
    l = s[edge].split( )
    edges.append((int(l[0]) - 1, int(l[1]) - 1))

  djSet = DisjointSet(num_nodes)
  for val1, val2 in edges:
    djSet.union(val1, val2)
  print djSet.num
   
if __name__ == '__main__':
  main()