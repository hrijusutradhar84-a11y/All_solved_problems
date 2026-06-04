"""
Breadth-First Search (BFS)

Problem: Implement BFS traversal for a graph. BFS explores vertices in layers - first all neighbors of 
the starting vertex, then their neighbors, and so on.

Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V)

Example:
    Graph: 0 -- 1 -- 2
           |        |
           3 ------+
    >>> bfs(graph, 0)
    [0, 1, 3, 2]
"""

from collections import deque

def bfs(graph, start):
    """
    Perform BFS traversal starting from a vertex.
    
    Args:
        graph (dict): Adjacency list representation of graph
        start (int): Starting vertex
    
    Returns:
        list: BFS traversal order
    """
    visited = set()
    queue = deque([start])
    result = []
    
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def bfs_with_distance(graph, start):
    """
    Perform BFS and calculate distance from start vertex.
    
    Args:
        graph (dict): Adjacency list representation
        start (int): Starting vertex
    
    Returns:
        dict: Vertex -> distance mapping
    """
    visited = {start: 0}
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited[neighbor] = visited[vertex] + 1
                queue.append(neighbor)
    
    return visited


def bfs_shortest_path(graph, start, end):
    """
    Find shortest path between two vertices using BFS.
    
    Args:
        graph (dict): Adjacency list representation
        start (int): Starting vertex
        end (int): Ending vertex
    
    Returns:
        list: Shortest path from start to end, or empty list if no path
    """
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        vertex, path = queue.popleft()
        
        if vertex == end:
            return path
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []


if __name__ == "__main__":
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    
    print("Test 1 (BFS):", bfs(graph, 0))                   # [0, 1, 3, 2]
    print("Test 2 (distances):", bfs_with_distance(graph, 0))  # {0: 0, 1: 1, 3: 1, 2: 2}
    print("Test 3 (shortest path):", bfs_shortest_path(graph, 0, 2))  # [0, 1, 2] or [0, 3, 2]
