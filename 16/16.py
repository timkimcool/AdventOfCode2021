def parse(data):
  return [line for line in data.splitlines()]
  
def partOne(data):
  strTot = ''
  for i in range(len(data)):
    strTot += bin(int(data[i], 16))[2:].zfill(4)
  vTot = 0
  count = 1
  strArr = [strTot]
  while strArr:
    curBin = strArr.pop(0)
    if '1' not in curBin:
      continue
    cat, val, strTot, vID = processBin(curBin)
    strArr.append(strTot)
    print("STEP: ", f'{cat=}, {strTot=}, {vID=}, {count=}, {val=}, {curBin=}')
    vTot += vID
    if cat == 3:
      count += int(val)
    if cat == 2:
      count += 1
      strArr.append(val)
    count -= 1
    print("DONE", count, strTot)
  return vTot

def processString(bin):
  vID = bin[:3]
  tID = bin[3:6]
  return vID, tID, bin[6:]

def processBin(bin):
  vID, tID, rest = processString(bin)
  print("Start", f'{bin=}, {rest=}, {tID=}')
  vID = int(vID, 2)
  if int(tID, 2) == 4:
    rest += '0' * (4 - len(rest)%4)
    newStr = ""
    while rest:
      subStr = rest[:5]
      print("SUB: ", subStr)
      newStr += subStr[1:5]
      if subStr[0] == '1':
        rest = rest[5:]
      else:
        rest = rest[5:]
        print("1", rest)
        return (1, int(newStr, 2), rest, vID)
  elif rest[0] == '0':
    length = rest[1:16]
    length = int(length, 2)
    print("2", length)
    return (2, rest[16:(16 + length)], rest[(16 + length):], vID)
  elif rest[0] == '1':
    packs = rest[1:12]
    print("3", int(packs, 2))
    return (3, packs, rest[12:], vID)
  print("fail")
  return "fail"
  
def partTwo(data):
  strTot = ''
  for i in range(len(data)):
    strTot += bin(int(data[i], 16))[2:].zfill(4)
  vTot = 0
  count = 1
  strArr = [strTot]
  while strArr:
    curBin = strArr.pop(0)
    if '1' not in curBin:
      continue
    cat, val, strTot, vID = processBin(curBin)
    strArr.append(strTot)
    print("STEP: ", f'{cat=}, {strTot=}, {vID=}, {count=}, {val=}, {curBin=}')
    vTot += vID
    if cat == 3:
      count += int(val)
    if cat == 2:
      count += 1
      strArr.append(val)
    count -= 1
    print("DONE", count, strTot)
  return vTot

def runCode(strTot):
  strArr = [strTot]
  while strArr:
    curBin = strArr.pop(0)
    if '1' not in curBin:
      continue
    cat, val, strTot, vID = processBin(curBin)
    strArr.append(strTot)
    print("STEP: ", f'{cat=}, {strTot=}, {vID=}, {count=}, {val=}, {curBin=}')
    vTot += vID
    if cat == 3:
      count += int(val)
    if cat == 2:
      count += 1
      strArr.append(val)
    count -= 1
    print("DONE", count, strTot)  

if __name__ == "__main__":
  with open('16/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    #print("Part Two: ", partTwo(data))