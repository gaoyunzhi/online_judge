# https://vijos.org/p/1002
import sys
def main():
  #  handle=sys.stdin
  handle = open("1002.txt", "r") 
  length_bridge = int(handle.readline())
  min_step, max_step, num_stone = map(int, handle.readline().split())
  stone_locations = map(int, handle.readline().split())
  stone_locations.sort()
  stone_locations.append(length_bridge)
  stone_locations = [0] + stone_locations
  new_stone_locations = [0]
  shorten = 0
  for index in xrange(num_stone + 1):
    if stone_locations[index + 1] - stone_locations[index] > min_step * max_step:
      shorten += ((stone_locations[index + 1] - stone_locations[index] - \
        min_step * max_step) / max_step)
    new_stone_locations.append(stone_locations[index + 1] - shorten * max_step)
  length_bridge = new_stone_locations[-1]
  del new_stone_locations[-1]
  del new_stone_locations[0]
  ans = [0]
  stone_locations = set(new_stone_locations)
  for i in xrange(1, length_bridge + max_step * min_step + 1):
    ans.append(min( \
      ans[max(0, i - max_step): max(-1, i - min_step) + 1] + [length_bridge] \
    ) + (i in stone_locations))
  sys.stdout.write(str(\
    min(ans[length_bridge: length_bridge + max_step * min_step + 1])
  ))
  
if __name__ == '__main__':
  main()