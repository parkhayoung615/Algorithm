N = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
cnt = []

for i in range(N):
    cnt.append(data[i]/data[0]*100)
    
print(sum(cnt) / N)