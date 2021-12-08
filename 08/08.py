def parse(data):
  return [line for line in data.splitlines()]
  
def partOne(data):
  data = parse(data)
  count = 0
  for line in data:
    list1 = line.split('|')[1].split(" ")
    for x in list1:
      if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
        count += 1
  return count

def partTwo(data):
  data = parse(data)
  totalSum = 0
  for line in data:
    lineList = line.split(' | ')
    strToNumDic = getStrDict(lineList[0].split(" "))
    tempSum = ''
    for code in lineList[1].split(" "):
      tempSum += str(strToNumDic[sortStr(code)])
    totalSum += int(tempSum)
  return totalSum

def getStrDict(list1):
  dict = {}
  dict2 = {}
  for x in range(len(list1)):
    if len(list1[x]) == 2:
      dict[1] = list1[x]
      dict2[sortStr(list1[x])] = 1
    elif len(list1[x]) == 3:
      dict[7] = list1[x]
      dict2[sortStr(list1[x])] = 7
    elif len(list1[x]) == 4:
      dict[4] = list1[x]
      dict2[sortStr(list1[x])] = 4
    elif len(list1[x]) == 7:
      dict[8] = list1[x]
      dict2[sortStr(list1[x])] = 8
  for x in range(len(list1)):
    if len(list1[x]) == 6:
      if not doesStrContain(dict[1], list1[x]):
        dict[6] = list1[x]
        dict2[sortStr(list1[x])] = 6
      elif doesStrContain(dict[4], list1[x]):
        dict[9] = list1[x]
        dict2[sortStr(list1[x])] = 9
      else:
        dict[0] = list1[x]
        dict2[sortStr(list1[x])] = 0
  for x in range(len(list1)):
    if len(list1[x]) == 5:
      if doesStrContain(dict[1], list1[x]):
        dict[3] = list1[x]
        dict2[sortStr(list1[x])] = 3
      elif doesStrContain(list1[x], dict[6]):
        dict[5] = list1[x]
        dict2[sortStr(list1[x])] = 5
      else: 
        dict[2] = list1[x]
        dict2[sortStr(list1[x])] = 2
  return dict2

def doesStrContain(str1, str2):
  list1 = list(str1)
  list2 = list(str2)
  for x in list1:
    if not x in list2:
      return False
  return True

def sortStr(str1):
  list1 = list(str1)
  list1.sort()
  return ''.join(list1)

if __name__ == "__main__":
  with open('08/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))