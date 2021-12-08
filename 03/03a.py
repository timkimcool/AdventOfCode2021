from collections import Counter

def partOne(data):
  theta = epsilon = ''
  for i in range(len(data)):
    counter = Counter([x[i] for x in data])
    if counter['0'] > counter['1']:
      theta += '0'
      epsilon += '1'
    else:
      theta += '1'
      epsilon += '0'
  return int(theta, 2) * int(epsilon, 2)

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
    data = f.read().strip().split('\n')
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))