def parse(data):
  return [line for line in data.splitlines()]
  
def partOne(data):
  grid, inst = data.split("\n\n")
  grid = parse(grid)
  grid.sort(key = lambda x: int(x.split(',')[0]), reverse = True)
  maxX = int(grid[0].split(',')[0]) + 1
  defLine = '.'*maxX
  grid.sort(key = lambda x: int(x.split(',')[1]))
  maxY = int(grid[-1].split(',')[1])
  gridDict = {}
  for line in grid:
    x, y = line.split(',')
    x = int(x)
    y = int(y)
    s = gridDict.get(y, defLine)
    s = s[:x] + '#' + s[x + 1:]
    gridDict[y] = s
  for y in range(maxY + 1):
    gridDict.setdefault(y, defLine)
  # for line in parse(inst):
  line = parse(inst)[0]
  instLine = line.split(' ')[2]
  var, num = instLine.split('=')
  if var == 'x':
    foldX(gridDict, int(num))
  else:
    foldY(gridDict, int(num))
  count = 0
  for key in gridDict:
    count += gridDict[key].count('#')
  return count

def foldX(gridDict, line):
  for key in gridDict:
    str = ''
    for count in range(1, line + 1):
      strLine = gridDict[key]
      try:
        str2 = '#' if strLine[line + count] == '#' or strLine[line - count] == '#' else '.'
      except IndexError:
        str2 = '#' if strLine[key + count] == '#' or strLine[key - count] == '#' else '.'
      str = str2 + str
    gridDict[key] = str
  return

def foldY(gridDict, line):
  for count in range(1, line + 1):
    try:
      gridDict[line - count] = combine(gridDict[line + count], gridDict[line - count])
    except KeyError:
      break
    del gridDict[line + count]
  del gridDict[line]
  return 

def combine(line1, line2):
  str = ''
  for i in range(len(line1)):
    str += '#' if line1[i] == '#' or line2[i] == '#' else '.'
  return str

def partTwo(data):
  grid, inst = data.split("\n\n")
  grid = parse(grid)
  grid.sort(key = lambda x: int(x.split(',')[0]), reverse = True)
  maxX = int(grid[0].split(',')[0]) + 1
  defLine = '.'*maxX
  grid.sort(key = lambda x: int(x.split(',')[1]))
  maxY = int(grid[-1].split(',')[1])
  gridDict = {}
  print(maxX, maxY)
  for line in grid:
    x, y = line.split(',')
    x = int(x)
    y = int(y)
    s = gridDict.get(y, defLine)
    s = s[:x] + '#' + s[x + 1:]
    gridDict[y] = s
  for y in range(maxY + 1):
    gridDict.setdefault(y, defLine)
  for line in parse(inst):
    instLine = line.split(' ')[2]
    var, num = instLine.split('=')
    print(var, num)
    if var == 'x':
      foldX(gridDict, int(num))
    else:
      foldY(gridDict, int(num))
  for i in range(len(gridDict.keys())):
    print(gridDict[i])
  return


if __name__ == "__main__":
  with open('13/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))