def sockMerchant(n, ar):
  cnt = 0
  odd_socks = []
  for sock in ar:
    if sock in odd_socks:
      odd_socks.remove(sock)
      cnt += 1
    else:
      odd_socks.append(sock)
  return cnt

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
