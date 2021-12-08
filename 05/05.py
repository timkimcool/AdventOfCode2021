def parse(data):
  return [line for line in data.splitlines()]

def partOne(data):
  dict = {}
  for line in data:
    num1, num2 = line.split(' -> ')
    x1, y1 = num1.split(',')
    x2, y2 = num2.split(',')
    if x1 == x2:
      ySmall = int(y1) if int(y1) < int(y2) else int(y2)
      yBig = int(y1) if int(y1) > int(y2) else int(y2)
      for y in range(ySmall, yBig + 1):
        if dict.get(f'{x1},{y}') == None:
          dict[f'{x1},{y}'] = 1
        else: dict[f'{x1},{y}'] += 1
    if y1 == y2:
      xSmall = int(x1) if int(x1) < int(x2) else int(x2)
      xBig = int(x1) if int(x1) > int(x2) else int(x2)
      for x in range(xSmall, xBig + 1):
        if dict.get(f'{x},{y1}') == None:
          dict[f'{x},{y1}'] = 1
        else: dict[f'{x},{y1}'] += 1
  count = 0
  for key in dict.keys():
    if dict[key] > 1:
      count += 1
  return count

def partTwo(data):
  dict = {}
  for line in data:
    num1, num2 = line.split(' -> ')
    x1, y1 = num1.split(',')
    x2, y2 = num2.split(',')
    ySmall = int(y1) if int(y1) < int(y2) else int(y2)
    yBig = int(y1) if int(y1) > int(y2) else int(y2)
    xSmall = int(x1) if int(x1) < int(x2) else int(x2)
    xBig = int(x1) if int(x1) > int(x2) else int(x2)
    if x1 == x2:
      for y in range(ySmall, yBig + 1):
        if dict.get(f'{x1},{y}') == None:
          dict[f'{x1},{y}'] = 1
        else: dict[f'{x1},{y}'] += 1
    elif y1 == y2:
      for x in range(xSmall, xBig + 1):
        if dict.get(f'{x},{y1}') == None:
          dict[f'{x},{y1}'] = 1
        else: dict[f'{x},{y1}'] += 1
    else:
      xInc = 1 if int(x1) < int(x2) else -1
      yInc = 1 if int(y1) < int(y2) else -1
      for inc in range(0, xBig - xSmall + 1):
        x = str(int(x1) + inc * xInc)
        y = str(int(y1) + inc * yInc)
        if dict.get(f'{x},{y}') == None:
          dict[f'{x},{y}'] = 1
        else: dict[f'{x},{y}'] += 1
  count = 0
  for key in dict.keys():
    if dict[key] > 1:
      count += 1
  return count

if __name__ == "__main__":
  with open('05/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(parse(data)))
    print("Part Two: ", partTwo(parse(data)))