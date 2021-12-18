def parse(data):
  return [line for line in data.splitlines()]
  
def partOne(data):
  data = parse(data)
  data = list(map(lambda x: list(map(int, list(x))), data))
  flash = 0
  flashed = {}
  for i in range(100):
    for key in flashed:
      x, y = key.split(',')
      data[int(x)][int(y)] = 0
    flashed = {}
    for x in range(len(data)):
      for y in range(len(data[x])):
        data[x][y] += 1
        queue = []
        if data[x][y] > 9:
          queue.append([x, y])
        while len(queue) > 0:
          curX, curY = queue.pop(0)
          if f'{curX},{curY}' in flashed:
            continue
          flashed[f'{curX},{curY}'] = 1
          flash += 1
          checkFlashes(curX, curY, queue, data) 
  return flash

def checkFlashes(curX, curY, queue, data):
  for x1 in range(-1, 2, 1):
    for y1 in range(-1, 2, 1):
      try:
        if data[curX + x1][curY + y1] > 9 or (x1 == 0 and y1 == 0) or curX + x1 < 0 or curY + y1 < 0:
          continue
        data[curX + x1][curY + y1] += 1
        if data[curX + x1][curY + y1] == 10:
          queue.append([curX + x1, curY + y1])
      except IndexError:
        continue   


def partTwo(data):
  data = parse(data)
  data = list(map(lambda x: list(map(int, list(x))), data))
  flashed = {}
  step = 0
  while len(flashed.keys()) != len(data) * len(data[0]):
    step += 1
    for key in flashed:
      x, y = key.split(',')
      data[int(x)][int(y)] = 0
    flashed = {}
    for x in range(len(data)):
      for y in range(len(data[x])):
        data[x][y] += 1
        queue = []
        if data[x][y] > 9:
          queue.append([x, y])
        while len(queue) > 0:
          curX, curY = queue.pop(0)
          if f'{curX},{curY}' in flashed:
            continue
          flashed[f'{curX},{curY}'] = 1
          checkFlashes(curX, curY, queue, data) 
  return step

def checkFlashes(curX, curY, queue, data):
  for x1 in range(-1, 2, 1):
    for y1 in range(-1, 2, 1):
      try:
        if data[curX + x1][curY + y1] > 9 or (x1 == 0 and y1 == 0) or curX + x1 < 0 or curY + y1 < 0:
          continue
        data[curX + x1][curY + y1] += 1
        if data[curX + x1][curY + y1] == 10:
          queue.append([curX + x1, curY + y1])
      except IndexError:
        continue   

if __name__ == "__main__":
  with open('11/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))