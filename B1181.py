data = []
for _ in range(int(input())):
    data.append(input())

data = list(set(data))
data.sort()
data.sort(key=lambda x: len(x))

for i in range(len(data)):
    print(data[i])