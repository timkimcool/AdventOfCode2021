import sys
import queue

def parse(data):
  return [int(l) for l in data.splitlines()]

def partOne(data) :
  count = 0
  prev = sys.maxsize
  for num in data:
    if int(prev) < num:
      count += 1
    prev = num
  return(count)

def partTwo(data):
  q = queue.Queue()
  count = 0
  prev = 0
  for num in data:
    q.put(num)
    prev += num
    if q.qsize() > 3:
      if prev - num < prev - q.get():
        count += 1
  return(count)

if __name__ == "__main__":
  with open('01/input.txt') as f:
    data = f.read()
    print("Part One: " + str(partOne(parse(data))))
    print("Part Two: " + str(partTwo(parse(data))))