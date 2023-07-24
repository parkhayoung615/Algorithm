import math

data = []
for i in range(5):
    data.append(int(input()))
    
data.sort()
print(math.trunc(sum(data) / 5), data[2])