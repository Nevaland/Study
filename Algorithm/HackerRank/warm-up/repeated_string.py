def repeatedString(s, n):
  cnt = 0
  s_len = len(s)
  cut_len = (n % s_len)
  full_repeated_num = (n // s_len)
  if full_repeated_num:
    cnt += s.count('a') * full_repeated_num
  cnt += s[:cut_len].count('a')

  return cnt

print(repeatedString('aba', 10))
print(repeatedString('a', 1000000000000))
