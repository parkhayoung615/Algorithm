s = list(map(str, input()))
data = []
for i in s:
    if(i.isupper()): data.append(i.lower())
    else: data.append(i.upper())

for i in data: print(i, end='')