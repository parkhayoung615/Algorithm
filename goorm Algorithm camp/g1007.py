#출석부

n, k = map(int,input().split()) # 사람의 수, k번째 사람

info = [] # n명의 사람의 이름과 키를 저장할 리스트
for _ in range(n):
	s,t = input().split() # 이름, 키
	info.append((s,float(t))) # tuple형으로 이름,키를 저장(문자열로 입력받았으므로 키는 float형으로 변환)
	
info = sorted(info, key = lambda x: (x[0],x[1])) # 1번째 기준: 문자열, 2번째 기준: 키
	
print(info[k-1][0], format(info[k-1][1],'.2f')) # 실수인 키는 소수 2번재짜리까지 출력