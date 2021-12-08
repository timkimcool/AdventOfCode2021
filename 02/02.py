def parse(data):
  return [line for line in data.splitlines()]

def partOne(data):
  forward = depth = 0
  for line in data:
    x, y = line.split()
    if x == 'forward':
      forward += int(y)
    else: 
      depth += int(y) if x == 'down' else -int(y)
  return forward * depth

def partTwo(data):
  forward = depth = aim = 0
  for line in data:
    x, y = line.split()
    if x == 'forward':
      forward += int(y)
      depth += aim * int(y)
    else: 
      aim += int(y) if x == 'down' else -int(y)
  return forward * depth

if __name__ == "__main__":
  with open('02/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(parse(data)))
    print("Part Two: ", partTwo(parse(data)))