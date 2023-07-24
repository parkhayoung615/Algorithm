eno = []
b = []
for i in range(3):
    eno.append(int(input()))
for i in range(2):
    b.append(int(input()))
print(min(eno) + min(b) - 50)
