#소수찾기

import math

def is_Prime(x):
	if x >= 2: # 2보다 큰 수만 소수인지 판별함
		for i in range(2, int(math.sqrt(x))+1): # n의 약수는 n의 제곱근 범위 안
			if x % i == 0: # i로 나누어 떨어지면 n은 소수 ㄴ
				return False
		return True
	else: # 2보다 작은 1과 0은 소수 ㄴ
		return False

n = int(input())
a = list(map(int,input().split()))

sum = 0
for i in range(1,n+1):
	if is_Prime(i): # i가 소수면 i번째 수인 a[i-1] 더함
		sum += a[i-1]
		
print(sum)