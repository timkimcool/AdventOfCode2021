def parse(data):
  return [line for line in data.splitlines()]

def partOne(data):
  dict = getCommonBitDict(data)
  gamma = getBinary(dict)
  epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])
  return int(gamma, 2) * int(epsilon, 2)

def getCommonBitDict(data):
  dict = {}
  for x in range(0, len(data[0])):
    dict[x] = 0
  for line in data:
    for x in range(0, len(line)):
      dict[x] += 1 if line[x] == "0" else -1
  return dict

def getBinary(dict):
  binary = ""
  for key in dict.keys():
    binary += "0" if int(dict[key]) > 0 else "1"
  return binary

def partTwo(data):
  oxy = getRating(data, "oxy")
  co2 = getRating(data, "co2")
  return int(oxy, 2) * int(co2, 2)

def getRating(data, type):
  numberList = data
  count = 0
  while len(numberList) != 1:
    list0 = []
    list1 = []
    for line in numberList:
      if line[count] == '1':
        list1.append(line)
      else: list0.append(line)
    if type == "oxy":
      numberList = list1 if len(list1) >= len(list0) else list0
    else: numberList = list1 if len(list1) < len(list0) else list0
    count += 1
  return numberList[0]


if __name__ == "__main__":
  with open('03/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(parse(data)))
    print("Part Two: ", partTwo(parse(data)))