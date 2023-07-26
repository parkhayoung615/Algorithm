# 알파벳 개수

s = list(input())
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
out = []

for i in range(len(arr)):
    cnt = 0
    for j in range(len(s)):
        if(s[j] == arr[i]):
            cnt += 1
    out.append(cnt)


for i in range(len(out)):
    print(out[i], end=' ')