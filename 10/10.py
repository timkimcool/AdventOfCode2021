def parse(data):
  return [line for line in data.splitlines()]
  
def partOne(data):
  data = parse(data)
  countTot = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0,
  }
  symbolDic = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
  }
  open = ['(', '[', '{', '<']  
  for line in data:
    queue = []
    for char in list(line):
      if char in open:
        queue.append(char)
      else:
        if queue[-1] != symbolDic[char]:
          countTot[char] += 1
          break
        else:
          queue.pop(-1)
  return getTotalScore(countTot)

def getTotalScore(countTot):
  multiplier = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
  }
  total = 0
  for symbol in countTot:
    total += countTot[symbol] * multiplier[symbol]
  return total



def partTwo(data):
  symbolDic = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
  }
  reverseSymbol = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
  }
  adder = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4,
  }
  open = ['(', '[', '{', '<']
  score = []
  for line in parse(data):
    queue = []
    for char in list(line):
      if char in open:
        queue.append(char)
      else:
        if queue[-1] != symbolDic[char]:
          queue = []
          break
        else:
          queue.pop(-1)
    if len(queue) > 0:
      total = 0
      for char in queue[::-1]:
        total = total * 5 + adder[reverseSymbol[char]]
      score.append(total)
  return sorted(score)[round(len(score)/2 -.5)]


if __name__ == "__main__":
  with open('10/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))