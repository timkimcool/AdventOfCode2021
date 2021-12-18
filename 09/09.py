def parse(data):
  return [line for line in data.splitlines()]
  
def partOne(data):
  data = parse(data)
  data = list(map(lambda x: list(map(int, list(x))), data))
  lowPtArray = []
  for x in range(len(data)):
    for y in range(len(data[x])):
      if checkIfLow(x, y, data):
        lowPtArray.append(data[x][y])  
  return sum(lowPtArray, len(lowPtArray))

def checkIfLow(x, y, data):
  curNumber = data[x][y]
  if (
    x > 0 and data[x - 1][y] <= curNumber or 
    x < len(data) - 1 and data[x + 1][y] <= curNumber or
    y > 0 and data[x][y - 1] <= curNumber or
    y < len(data[x]) - 1 and data[x][y + 1] <= curNumber
  ):
    return False
  return True

def partTwo(data):
  data = parse(data)
  data = list(map(lambda x: list(map(int, list(x))), data))
  visited = {}
  queue = []
  basinSizes = []
  #basins = []
  for x in range(len(data)):
    for y in range(len(data[x])):
      if f'{x},{y}' in visited or data[x][y] == 9:
        continue
      queue.append([x, y])
      size = 0
      #basin = []
      while len(queue) > 0:
        curCoord = queue.pop(0)
        curX, curY = curCoord
        if f'{curX},{curY}' in visited:
          continue
        checkBasin(curX, curY, data, visited, queue)
        #basin.append(f'{curX},{curY}:{data[curX][curY]}')
        size += 1
      #basins.append(basin)
      basinSizes.append(size)
  basinSizes.sort()
  return basinSizes[-1] * basinSizes[-2] * basinSizes[-3]

def checkBasin(curX, curY, data, visited, queue):
  if curX < len(data) - 1 and f'{curX + 1},{curY}' not in visited:
      if data[curX + 1][curY] == 9:
        visited[f'{curX + 1},{curY}'] = 1
      else:
        queue.append([curX + 1, curY])
  if curX > 0 and f'{curX - 1},{curY}' not in visited:
      if data[curX - 1][curY] == 9:
        visited[f'{curX - 1},{curY}'] = 1
      else:
        queue.append([curX - 1, curY])
  if curY < len(data[curX]) - 1 and f'{curX},{curY + 1}' not in visited:
      if data[curX][curY + 1] == 9:
        visited[f'{curX},{curY + 1}'] = 1
      else:
        queue.append([curX, curY + 1])
  if curY > 0 and f'{curX},{curY - 1}' not in visited:
      if data[curX][curY - 1] == 9:
        visited[f'{curX},{curY - 1}'] = 1
      else:
        queue.append([curX, curY - 1])
  visited[f'{curX},{curY}'] = 1
  return


if __name__ == "__main__":
  with open('09/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))