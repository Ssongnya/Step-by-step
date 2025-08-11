# BFS (너비 우선 탐색)

## BFS(너비 우선 탐색) 특징

### 그래프 탐색 방법

- DFS(깊이 우선 탐색) : Stack 활용

#### BFS(Breadth First Search, 너비 우선 탐색)

- **큐 활용**
- 시작점의 인접한 정점들을 모두 차례로 방문한 후 방문했던 정점을 시작점으로하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들을 탐색한 후, 차례로 너비 우선 탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐 활용

### BFS(너비 우선 탐색)이 탐색하는 순서

- gif 짤영상 넣기

### 입력 파라미터 : 그래프 G와 탐색 시작점 v

```python
def BFS(G, v):  # 그래프 G, 탐색 시작점 v
    visited = [0] * n   # n : 정점의 개수
    queue = []  # 큐 생성
    queue.append(v)     # 시작점 v를 큐에 삽입
    while queue :   #큐가 비어있지 않은 경우
        t = queue.pop(0) # 큐의 첫번째 원소 반환
        if not visited[t] :   # 방문되지 않은 곳이라면
            visited[t] = True   # 방문한 것으로 표시
            visit(t)
        for i in G[t] : # t와 연결된 모든 선에 대해
            if not visited[i] :  # 방문되지 않은 곳이라면
                queue.append(i)  # 큐에 넣기
```

## BFS(너비 우선 탐색) 알고리즘

예시)

```
  - B - E, F
A - C 
  - D - G, H, I
```

1. 초기 상태
- visited 리스트 초기화
- Q 생성
- 시작점 enQueue

2. A점부터 시작
- deQueue A
- A 방문한 것으로 표시
- A의 인접점인 B, C, D를 큐에 삽입 enQueue

3. 탐색 진행
- deQueue B - B를 큐에서 삭제하고
- B 방문한 것으로 표시
- B의 인접점인 E, F를 큐에 삽입 enQueue

4. 탐색 진행
- deQueue C
- C 방문한 것으로 표시
- C의 인접점 enQueue (없을 경우에는 원소 추가X)

5. 탐색 진행
- deQueue D
- D 방문한 것으로 표시
- D의 인접점 G, H, I enQueue

6. 탐색 진행
- deQueue E
- E 방문한 것으로 표시
- E의 인접점 X
- 같은 방법으로 F, G, H, I 방문
- I 방문 후에는 큐가 비었으므로 탐색 종료

