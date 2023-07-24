data = []
tot = {}

for i in range(10):
    data.append(int(input()))
    data[i] = data[i] % 42

for i in data:
    try : tot[i] += 1
    except: tot[i] = 1
print(len(tot))