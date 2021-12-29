def parse(data):
  return [line for line in data.splitlines()]
  
def partOne(data):
  data = parse(data)
  newPolymer = makePolymer(makeDic(data), data[0], 10)
  counted = countCharacters(newPolymer)
  return counted[-1] - counted[0]

def makePolymer(dic, polymer, count):
  for num in range(count):
    newPolymer = polymer[0]
    for i in range(1, len(polymer)):
      pair = polymer[i - 1] + polymer[i]
      if pair in dic:
        newPolymer += dic[pair] + pair[1] if pair in dic else pair[1]
    polymer = newPolymer
  return polymer

def makeDic(data):
  dic = {}
  for line in range(2, len(data)):
    pair, insert = data[line].split(' -> ')
    dic[pair] = insert
  return dic

def countCharacters(polymer):
  charCounter = {}
  for char in polymer:
    if char in charCounter:
      charCounter[char] += 1
    else:
      charCounter[char] = 1
  return sorted(list(charCounter.values()))
  
def partTwo(data):
  data = parse(data)
  polymer = data[0]
  rules = makeDic(data)
  rules10 = make10Dic(rules)
  for count in range(2):
    print(count)
    newPolymer = polymer[0]
    for i in range(1, len(polymer)):
      pair = polymer[i - 1] + polymer[i]
      if pair in rules10:
        newPolymer += rules10[pair] + pair[1] if pair in rules10 else pair[1]
    polymer = newPolymer
  counted = countCharacters(polymer)
  return counted[-1] - counted[0]

def make10Dic(rules):
  rules10 = {}
  rules20 = {}
  rules40 = {}
  for key in rules:
    print('10', key)
    rules10[key] = makePolymer(rules, key, 10)
  print(rules10)
  for key in rules:
    print('20', key)
    rules20[key] = makePolymer(rules10, key, 2)
  print(rules20)
  for key in rules:
    print('40', key)
    rules40[key] = makePolymer(rules20, key, 2)
  print(rules40)
  return rules40

if __name__ == "__main__":
  with open('14/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))