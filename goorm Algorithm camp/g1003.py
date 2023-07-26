#동명이인

n, m = input().split() # input 기본값 문자열
c = 0

for i in range(int(n)):
    name = input()
    if m in name:
        c += 1
print(c)