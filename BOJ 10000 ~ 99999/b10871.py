N, X = map(int, input().split())
data = list(map(int, input().split()))

for i in range (len(data)):
    if (data[i] < X):
        print(data[i], end=' ')