    for i in indexNumToLine[num]:
      indexLineToNum[i].remove(num)
      if len(indexLineToNum[i]) == 0:
        return getRemainingSum(i, indexLineToNum) * int(num)