import pandas as pd
df = pd.read_csv('01/input.txt', header=None, names=['value'])

part1 = sum(df.value > df.value.shift()) 
part2 = sum(df.value.rolling(3).sum() > df.value.rolling(3).sum().shift())

print(f'Part One: {part1}\nPart Two: {part2}')