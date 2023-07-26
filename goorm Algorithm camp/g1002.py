#경로의 개수

n = int(input()) # 섬의 개수
n_list = list(map(int, input().split())) # 각 섬의 다리의 개수(공백으로 구분)

case = 1
for i in n_list:
	case *= i # 각 섬의 다리의 개수를 모두 곱해줌

print(case)