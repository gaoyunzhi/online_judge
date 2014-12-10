# https://vijos.org/p/1002

def main():
  #  handle=sys.stdin
  handle = open("1002.txt", "r") 
  length_bridge = int(handle.readline())
  min_step, max_step, num_stone = map(int, handle.readline().split())
  stone_locations = map(int, handle.readline().split())[:num_stone]
  stone_locations.sort()
  stone_locations.append(length_bridge)
  for index in xrange(len(stone_locations) - 1):
    if stone_locations[index + 1] - stone_locations[index] > min_step * max_step:
      shorten = (stone_locations[index + 1] - stone_locations[index] - \
        min_step * max_step) / max_step
      stone_locations[index + 1] -= shorten * max_step
  length_bridge = stone_locations[-1]
  del stone_locations[-1]
  ans = [0]
  stone_locations = set(stone_locations)
  for i in xrange(1, length_bridge + max_step * min_step + 1):
    ans.append(min( \
      ans[max(0, i - max_step): max(-1, i - min_step) + 1] + [length_bridge] \
    ) + (i in stone_locations))
  print min(ans[length_bridge: length_bridge + max_step * min_step + 1])
  
if __name__ == '__main__':
  main()