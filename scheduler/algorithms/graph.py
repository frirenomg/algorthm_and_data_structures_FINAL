class TaskGraph:
    def __init__(self):
        self.graph = {}

    def add_task(self, task_id):
        if task_id not in self.graph:
            self.graph[task_id] = []

    def add_dependency(self, task, depends_on):
        self.graph[depends_on].append(task)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbour in self.graph.get(start, []):
            if neighbour not in visited:
                self.dfs(neighbour, visited)
        return visited

from collections import deque

def bfs(self, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        for n in self.graph.get(node, []):
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return visited
