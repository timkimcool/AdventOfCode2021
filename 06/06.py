def partOne(data):
  list = data.split(',')
  dict = initDict(list)
  for _ in range(80):
    applyDay(dict)
  return sumDict(dict)

def initDict(list):
  dict = {}
  for i in range(9):
    dict[i] = 0
  for num in list:
    dict[int(num)] += 1
  return dict

def sumDict(dict):
  count = 0
  for d in range(9):
    count += dict[d]
  return count

def applyDay(dict):
  for i in range(9):
    dict[i - 1] = dict [i]
  dict[8] = dict[-1]
  dict[6] += dict[-1]
  return dict

def partTwo(data):
  list = data.split(',')
  dict = initDict(list)
  for _ in range(256):
    applyDay(dict)
  return sumDict(dict)

if __name__ == "__main__":
  with open('06/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))