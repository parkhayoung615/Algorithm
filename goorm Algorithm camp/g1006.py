#철자 분리 집합

n = int(input()) # 문자열의 길이
arr = input() # 문자열
cnt = 0 # 분리 횟수
for i in range(n-1):
    if arr[i+1] == arr[i]: # 다음 문자와 같은 경우
        continue
    else: # 다음 문자와 다른 경우 분리 횟수 +1
        cnt += 1

print(cnt+1)