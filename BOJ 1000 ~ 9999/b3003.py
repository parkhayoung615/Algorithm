c = [1, 1, 2, 2, 2, 8]

a = list(map(int, input().split()));
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
for i in range(6):
    print(c[i] - a[i], end=' ')
