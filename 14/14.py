from collections import Counter

def parse(data):
  return [line for line in data.splitlines()]
  
def partOne(data):
  data = parse(data)
  rules = [r.split(" -> ") for r in data[2:]]
  rules = {a: (a[0] + b, b + a[1]) for a,b in rules}
  pairs = ["".join(p) for p in zip(data[0], data[0][1:])]

  pairCtr = runSteps(pairs, rules, 10)
  count = countLetters(pairCtr)
  count[data[0][-1]] += 1
  return max(count.values()) - min(count.values())

def runSteps(pairs, rules, steps):
  pairCtr = Counter(pairs)
  for _ in range(steps):
    for key, value in pairCtr.copy().items():
      pairCtr[rules[key][0]] += value
      pairCtr[rules[key][1]] += value
      pairCtr[key] -= value
  return pairCtr

def countLetters(pairCtr):
  letterCount = {}
  for (a, b), c in pairCtr.items():
    letterCount[a] = letterCount.get(a, 0) + c
  return letterCount
  
def partTwo(data):
  data = parse(data)
  rules = [r.split(" -> ") for r in data[2:]]
  rules = {a: (a[0] + b, b + a[1]) for a,b in rules}
  pairs = ["".join(p) for p in zip(data[0], data[0][1:])]

  pairCtr = runSteps(pairs, rules, 40)
  count = countLetters(pairCtr)
  count[data[0][-1]] += 1
  return max(count.values()) - min(count.values())

if __name__ == "__main__":
  with open('14/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))