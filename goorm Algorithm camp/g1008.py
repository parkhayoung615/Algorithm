#폭탄 구현

import numpy as np

n, k = map(int, input().split()) # 정사각형 한 변의 길이, 폭탄의 개수
list1 = [[0] * (n + 2)] * (n + 2) # 그림과 같이 첫번째 칸을 [1][1], 마지막칸을 [n][n]으로 사용하기 위해 위아래, 좌우를 각각 +1씩한 (n+2)*(n+2)의 2차원 배열을 만들어줌 
arr=np.array(list1)

for _ in range(k):
	a, b = map(int,input().split()) # 폭탄이 떨어질 위치
	
	# 폭탄에 영향을 받는 상하좌우에 +1
	arr[a][b]+=1
	arr[a][b+1]+=1
	arr[a][b-1]+=1
	arr[a+1][b]+=1
	arr[a-1][b]+=1

bomb=arr[1:(n + 1), 1:(n + 1)] # [1][1]부터 [n][n]까지만 잘라내기
print(np.sum(bomb))