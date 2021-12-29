def parse(data):
  return [line for line in data.splitlines()]
  
def partOne(data):
  data = parse(data)
  yMax = len(data)
  xMax = len(data[0])
  map = {}
  shortestPath = {}
  for y, line in enumerate(data):
    for x, val in enumerate(list(line)):
      map[f'{x}, {y}'] = int(val)
  shortestPath['0, 0'] = map['0, 0']
  for y in range(yMax):
    for x in range(xMax):
      curVal = shortestPath.get(f'{x + 1}, {y}', 0)
      newVal = shortestPath[f'{x}, {y}'] + map[f'{x + 1}, {y}']
      if not curVal or newVal < curVal:
        shortestPath[f'{x + 1}, {y}'] = newVal
      curVal = shortestPath.get(f'{x}, {y + 1}', 0)
      newVal = shortestPath[f'{x}, {y}'] + map[f'{x}, {y + 1}']
      if not curVal or newVal < curVal:
        shortestPath[f'{x}, {y + 1}'] = newVal
  print(shortestPath)
  return min(shortestPath[f'{xMax - 1}, {yMax - 2}'], shortestPath[f'{xMax - 2}, {yMax - 1}']) + map[f'{xMax - 1}, {yMax - 1}'] - map['0, 0']

def partTwo(data):
  data = parse(data)
  polymer = data[0]
  rules = makeDic(data)
  rules10 = make10Dic(rules)
  for count in range(2):
    print(count)
    newPolymer = polymer[0]
    for i in range(1, len(polymer)):
      pair = polymer[i - 1] + polymer[i]
      if pair in rules10:
        newPolymer += rules10[pair] + pair[1] if pair in rules10 else pair[1]
    polymer = newPolymer
  counted = countCharacters(polymer)
  return counted[-1] - counted[0]

if __name__ == "__main__":
  with open('15/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    #print("Part Two: ", partTwo(data))