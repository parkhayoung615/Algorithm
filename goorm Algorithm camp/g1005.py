#합격자 찾기

t = int(input()) # 시험의 개수
for i in range(t):
	n = int(input()) # 응시 인원 수
	value = list(map(int, input().split())) # 시험 성적
	avg = sum(value)/len(value) # 평균 성적
	c = 0 # 합격자
	for v in value:
		if v >= avg:
			c += 1
	print("%d/%d"%(c, n))