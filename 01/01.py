def parse(data):
  return [int(l) for l in data.splitlines()]

def partOne(data):
  if len(data) < 2:
    return 0
  return sum(x < y for x, y in zip(data, data[1:]))

def partTwo(data):
  if len(data) < 4:
    return 0
  return sum(n1 < n4 for n1, n4 in zip(data, data[3:]))

if __name__ == "__main__":
  with open('01/input.txt') as f:
    data = f.read()
    print("Part One: " + str(partOne(parse(data))))
    print("Part Two: " + str(partTwo(parse(data))))