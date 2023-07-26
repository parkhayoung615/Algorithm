#BFS 너비 우선 탐색

from collections import deque

graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
Q = deque()

visited[1] = 1
Q.append(1)

while Q:
	cur = Q.popleft()
	for next in graph[cur]:
		if visited[next]:
			continue
		visited[next] = 1
		Q.append(next)
		


#BFS 2

from collections import deque

# BFS
def bfs(graph, start, visited):
	# 큐 구현을 위해 deque 라이브러리 사용
	queue = deque([start])
	# 현재 노드를 방문 처리
	visited[start] = True

	# 큐가 빌때까지 반복
	while queue:
		v = queue.popleft()
		print(v, end=' ')
		# 해당 원소와 인접한, 아직 방문하지 않은 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

# 인접 리스트 : 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
			[], # 0번 노드와 인접한 노드
    		[2, 3, 8],
    		[1, 7],
    		[1, 4, 5],
    		[3, 5],
    		[3, 4],
    		[7],
    		[2, 6, 8],
    		[1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)

# 출력결과 : 1 2 3 8 7 4 5 6




#BFS 3

from collections import deque
def bfs(maps,x,y):
    queue=deque()
    xy=[(-1,0),(1,0),(0,-1),(0,1)]
    max_maps = [[0] * len(maps[0]) for _ in range(len(maps))]
    
    queue.append((x,y))
    max_maps[x][y]=1
    while queue:
        x,y = queue.popleft()
        if x==len(maps) and y==len(maps[0]):
            break
        for i in range(len(xy)):
            nx = x+xy[i][0]
            ny = y+xy[i][1]
            
            if (nx>=0) and (ny>=0) and (nx<len(maps)) and (ny<len(maps[0])):
                if (maps[x][y]==1 and max_maps[nx][ny]==0):
                    queue.append((nx,ny))
                    max_maps[nx][ny] = max_maps[x][y] + 1
                
    return max_maps[len(maps)-1][len(maps[0])-1]
                
def solution(maps):
    if not bfs(maps,0,0):
        return -1
    return bfs(maps,0,0)




#BFS 4

from collections import deque 
visited = [False] * 10 

def bfs(v): 
    q = deque([v]) 
    visited[v] = True 
    
    while q: # 큐가 비지 않는 동안 
        a = q.popleft() 
        print(a,end=' ') 
        w = sorted(graph[a]) # 번호가 작은 곳부터 순서대로 방문하기 위해 정렬 
        for i in w: 
            if not visited[i]: 
                q.append(i) # 방문할 곳 append 
                visited[i] = True # 방문한 곳 check