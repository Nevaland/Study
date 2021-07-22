def jumpingOnClouds(c):
  jump_cnt = 0
  SAFE = 0
  UNSAFE = 1
  visitable_clouds = []
  for i, is_safe in enumerate(c):
    if is_safe == SAFE:
      visitable_clouds.append(i)

  prev_jump_distance = 0
  for cloud_i in range(1, len(visitable_clouds)):
    jump_distance = visitable_clouds[cloud_i] - visitable_clouds[cloud_i-1]
    jump_cnt += 1
    if (jump_distance + prev_jump_distance) <= 2 and prev_jump_distance != 0: # sum eqaul 2
      jump_cnt -= 1
      prev_jump_distance = jump_distance + prev_jump_distance
    else:
      prev_jump_distance = jump_distance
  return jump_cnt

print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))
