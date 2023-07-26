a, b = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
    
print(data[b-1])