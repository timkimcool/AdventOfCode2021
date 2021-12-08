def partOne(data):
  list1 = list(map(int, data.split(',')))
  median = getMedian(list1)
  count = 0
  for num in list1:
    count += abs(num - median)
  return count

def getMedian(list1):
  list1.sort()
  median = list1[int(len(list1)/2)]
  return median

def partTwo(data):
  list1 = list(map(int, data.split(',')))
  list1.sort()
  dict = initDict(list1)
  fuelTotal = 0
  while len(dict) != 1:
    list1 = list(dict)
    list1.sort()
    fuelL = sumFuel(dict[list1[0]])
    fuelR = sumFuel(dict[list1[len(list1) - 1]])
    if fuelL < fuelR:
      inc = 1
      fuelTotal += fuelL
      index = 0
    else:
      inc = -1
      fuelTotal += fuelR
      index = len(list1) - 1
    if dict.get(list1[index] + inc) == None:
      dict[list1[index] + inc] = {}
    for key in list(dict[list1[index]]):
      dict[list1[index] + inc][key + 1] = dict[list1[index]][key]
    del dict[list1[index]]
    list1.pop(index)
  return fuelTotal

def initDict(list1):
  dict = {}
  for num in list1:
    if dict.get(num) != None:
      dict[num][1] += 1
    else: dict[num] = { 1: 1 }
  return dict
  
def sumFuel(dict):
  fuel = 0
  for key in dict.keys():
    fuel += key * dict[key]
  return fuel

if __name__ == "__main__":
  with open('07/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))