#뿌요뿌요

N,M = map(int, input().split())
matrix = [[0 for _ in range(N)] for _ in range(N)]
flag = True
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(M):
    stone_index, stone_type = map(int, input().split())
    stone_index -= 1
    for j in range(N-1, -1, -1):
        if matrix[j][stone_index] == 0:
            matrix[j][stone_index] = stone_type
            for k in range(4):
                next_j = j + dy[k]
                next_i = stone_index + dx[k]
                if 0 <= next_i < N and 0 <= next_j < N:
                    if matrix[next_j][next_i] == stone_type:
                        matrix[j][stone_index] = 0
                        matrix[next_j][next_i] = 0
                        for l in range(N-1, 0, -1):
                            if matrix[l][next_i] == 0 and matrix[l-1][next_i] != 0:
                                matrix[l][next_i] = matrix[l-1][next_i]
                                matrix[l-1][next_i] = 0
            break
        elif j == 0 and matrix[j][stone_index] != 0:
            flag = False
if flag:
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()
else:
    print('패배')