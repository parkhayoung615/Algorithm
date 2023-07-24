a = []
for i in str(input()):
    a.append(int(i))
a.sort(reverse=True)

for i in range(len(a)):
    print(a[i], end='')