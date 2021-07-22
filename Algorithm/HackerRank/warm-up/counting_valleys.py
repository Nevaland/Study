def countingValleys(steps, path):
  altitude = 1
  valley_cnt = 0
  in_valley = False
  
  for direction in path:
    if direction == 'U':
      altitude += 1
    elif direction == 'D':
      altitude -= 1

    if in_valley and 1 <= altitude:
      in_valley = False
    elif not in_valley and altitude < 1:
      in_valley = True
      valley_cnt += 1
    
  return valley_cnt

print(countingValleys(12, "DDUUDDUDUUUD"))
