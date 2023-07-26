#DFS 깊이 우선 탐색

graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

def DFS(cur):
	for next in graph[cur]:
		if visited[next]:
			continue
		visited[next] = 1
		DFS(next)

visited[1] = 1
DFS(1)



# DFS 2

def dfs(v): 
    if visited[v]: 
        return 
    visited[v] = True 
    print(v,end = ' ') 
    w = sorted(graph[v])
    for i in w: 
    	if not visited[i]: 
        	dfs(i)