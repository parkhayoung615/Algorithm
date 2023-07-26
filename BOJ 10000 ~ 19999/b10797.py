#10부제

n = int(input())
s = list(map(int, input().split()))
cnt = 0

for i in range(len(s)):
    if(n == s[i]):
        cnt += 1
print(cnt)