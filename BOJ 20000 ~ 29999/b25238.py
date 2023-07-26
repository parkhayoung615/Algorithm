n, m = map(int, input().split(' '))
print(0 if (n - (m/100 * n)) >= 100.0 else 1)