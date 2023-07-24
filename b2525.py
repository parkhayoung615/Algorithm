H, N = map(int, input().split())
t = int(input())

H += t // 60
N += t % 60

if N >= 60:
    H += 1
    N -= 60
if H >= 24:
    H -= 24

print(H, N, end='')