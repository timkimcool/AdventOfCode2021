from pathlib import Path
import sys
import queue


q = queue.Queue()

count = 0
prev = 0
for line in open(Path.cwd() / '01' / 'input.txt').readlines():
  num = int(line.strip())
  q.put(num)
  prev += num
  if q.qsize() > 3:
    if prev - num < prev - q.get():
      count += 1
print(count)