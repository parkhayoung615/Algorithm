sum = 1
for i in range(3):
    i = int(input())
    sum *= i
tot = str(sum)

for sum in range(10):
    print(tot.count(str(sum)))
