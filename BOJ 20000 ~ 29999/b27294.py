n, m = map(int, input().split(' '))
if (m == 1 or n <= 11 or n >= 17):
  print(280)

elif (n >= 12 and n <= 16 and m == 0):
  print(320)