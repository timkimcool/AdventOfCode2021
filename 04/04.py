def parse(data):
  return [line for line in data.splitlines()]

def partOne(data):
  seq = data[0]
  indexToLine, numToIndex = getDictOfAllRowsAndColumns(data)
  for num in seq.split(','):
    if numToIndex.get(num) != None:
      for line in numToIndex[num]:
        indexToLine[line].remove(num)
        if len(indexToLine[line]) == 0:
          return getRemainingSum(line, indexToLine) * int(num)

def getDictOfAllRowsAndColumns(data):
  #Line = boardNum-LineNum (0-4 horizontal, 5-9 vertical)
  indexToLine = {} #{0-1: [1, 2, 3, 4, 5]}
  numToIndex = {} # {3: ['0-1', ...]}
  count = 0
  for x in range(0, 100):
    numToIndex[str(x)] = []
  for boardNum in range(2, len(data), 6):
    columnList = [ [] for _ in range(5) ]
    for lineNum in range(0, 5):
      rowList = data[boardNum + lineNum].split()
      for numIndex in range(0, 5):
        numToIndex[rowList[numIndex]].append(f'{count}-{lineNum}')  #add row index
        numToIndex[rowList[numIndex]].append(f'{count}-{5 + numIndex}') #add column index
      indexToLine[f'{count}-{lineNum}'] = rowList
      for num in range(0, 5):
        columnList[num].append(rowList[num])
    for line in range(0, 5):
      indexToLine[f'{count}-{5 + line}'] = columnList[line]
    count += 1
  return indexToLine, numToIndex

def getRemainingSum(line, indexToLine):
  boardNum = line.split('-')[0]
  sum = 0
  for rowNum in range(0, 5):
    if indexToLine.get(f'{boardNum}-{rowNum}') != None:
      for num in indexToLine[f'{boardNum}-{rowNum}']:
        sum += int(num)
  return sum


def partTwo(data):
  bingoNumbers = data[0]
  indexToLine, numToIndex = getDictOfAllRowsAndColumns(data)
  for num in bingoNumbers.split(','):
    if numToIndex.get(num) != None:
      for boardIndex in numToIndex[num]:
        if indexToLine.get(boardIndex) != None:
          indexToLine[boardIndex].remove(num)
          if len(indexToLine) == 10:
            return getRemainingSum(boardIndex, indexToLine) * int(num)
          deleteWinningBoards(boardIndex, indexToLine)
            
def deleteWinningBoards(boardIndex, indexToLine):
  if len(indexToLine[boardIndex]) == 0:
    boardNum = boardIndex.split('-')[0]
    for line in range(0, 10):
      del indexToLine[f'{boardNum}-{line}']
  return

if __name__ == "__main__":
  with open('04/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(parse(data)))
    print("Part Two: ", partTwo(parse(data)))