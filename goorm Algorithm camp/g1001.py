#최장 맨해튼 거리

import sys
input = sys.stdin.readline
arr = list(map(int, input().split()))
arr.sort()
x = abs(arr[0] - arr[3])
y = abs(arr[1] - arr[2])

print(x + y)