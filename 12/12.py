def parse(data):
  return [line for line in data.splitlines()]
  
def partOne(data):
  data = parse(data)
  vertices = {}
  initilaizeDict(data, vertices)
  routes = []
  routing = { '0': { 'visited': { 'start': 1 }, 'route': ['start'] }}
  i = 0
  while len(routing.keys()) > 0:
    for key in list(routing):
      last = routing[key]['route'][-1]
      if last in vertices:
        for out in vertices[last]['out']:
          if out == 'end':
            routes.append(routing[key]['route'].copy() + ['end'])
          elif out not in routing[key]['visited']:
            i += 1
            routing[i] = { 'visited': routing[key]['visited'].copy(), 'route': routing[key]['route'].copy() + [out]}
            if out.islower():
              routing[i]['visited'][out] = 1
      routing.pop(key)
  return len(routes)

def initilaizeDict(data, vertices):
  for line in data:
    start, end = line.split('-')
    if start in vertices:
      vertices[start]['out'].append(end)
    else:
      vertices[start] = {'out': [end]}
    if end in vertices:
      vertices[end]['out'].append(start)
    else:
      vertices[end] = {'out': [start]}
  return

def partTwo(data):
  data = parse(data)
  vertices = {}
  initilaizeDict(data, vertices)
  routes = []
  routing = { '0': { 'visited': { 'start': 2 }, 'route': ['start'], 'visitedSmall': False }}
  i = 0
  while len(routing.keys()) > 0:
    for key in list(routing):
      last = routing[key]['route'][-1]
      if last in vertices:
        for out in vertices[last]['out']:
          if out == 'end':
            routes.append(routing[key]['route'].copy() + ['end'])
          elif out == 'start':
            continue
          elif out not in routing[key]['visited'] or not routing[key]['visitedSmall']:
            i += 1
            routing[i] = { 'visited': routing[key]['visited'].copy(), 'route': routing[key]['route'].copy() + [out], 'visitedSmall': routing[key]['visitedSmall'] and True}
            if out.islower():
              if out in routing[i]['visited']:
                routing[i]['visitedSmall'] = True
              else:
                routing[i]['visited'][out] = 1
      routing.pop(key)
  return len(routes)

if __name__ == "__main__":
  with open('12/input.txt') as f:
    data = f.read()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))