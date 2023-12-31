## 0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, ...
## 策略：
## 偶數項 4, 7, 10....(3(n/2)+1)
## 奇數項 3, 6, 9，先抓到其對應的偶數項 n-1 的值，再扣 1 起來

def get_number(index):
  n = index + 1
  if n == 1:
    return 0
  elif n%2 == 0:
    return int(3*( n / 2 ) + 1)
  else:
    oddGuy = 3*( (n-1) / 2 ) + 1
    return int(oddGuy - 1)
  


result = get_number(1) # print 4
# result = get_number(5) # print 10
# result = get_number(10) # print 15