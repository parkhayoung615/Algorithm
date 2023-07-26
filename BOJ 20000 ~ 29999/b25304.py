tot = int(input())
N = int(input())
tot2 = 0

for _ in range(N):
    A, B = map(int, input().split())
    tot2 = A * B + tot2
    
if tot == tot2:
    print("Yes")
else:
    print("No")