from pathlib import Path
import sys

count = 0
prev = sys.maxsize
for line in open(Path.cwd() / '01' / 'input.txt').readlines():
  num = int(line.strip())
  if int(prev) < num:
    count += 1
  prev = num
print(count)