#세수정렬

s = list(map(int, input().split()))
s.sort()
for i in range(len(s)):
    print(s[i], end=' ')