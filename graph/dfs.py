"""
Depth-First Search (DFS)

Problem: Implement DFS traversal for a graph. DFS explores as far as possible along each branch before 
backtracking.

Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V)

Example:
    Graph: 0 -- 1 -- 2
           |        |
           3 ------+
    >>> dfs(graph, 0)
    [0, 1, 2, 3]
"""

def dfs_recursive(graph, start, visited=None):
    """
    Perform DFS traversal using recursion.
    
    Args:
        graph (dict): Adjacency list representation
        start (int): Starting vertex
        visited (set): Set of visited vertices
    
    Returns:
        list: DFS traversal order
    """
    if visited is None:
        visited = set()
    
    result = []
    
    def dfs_helper(vertex):
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs_helper(neighbor)
    
    dfs_helper(start)
    return result


def dfs_iterative(graph, start):
    """
    Perform DFS traversal using iterative approach (stack).
    
    Args:
        graph (dict): Adjacency list representation
        start (int): Starting vertex
    
    Returns:
        list: DFS traversal order
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors in reverse order for consistent ordering
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


def dfs_all_paths(graph, start, end, visited=None):
    """
    Find all paths between two vertices using DFS.
    
    Args:
        graph (dict): Adjacency list representation
        start (int): Starting vertex
        end (int): Ending vertex
        visited (set): Set of visited vertices
    
    Returns:
        list: All paths from start to end
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    paths = []
    
    if start == end:
        return [[end]]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            for path in dfs_all_paths(graph, neighbor, end, visited.copy()):
                paths.append([start] + path)
    
    return paths


if __name__ == "__main__":
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    
    print("Test 1 (DFS recursive):", dfs_recursive(graph, 0))  # [0, 1, 2, 3]
    print("Test 2 (DFS iterative):", dfs_iterative(graph, 0))  # [0, 1, 2, 3]
    print("Test 3 (all paths):", dfs_all_paths(graph, 0, 2))  # [[0, 1, 2], [0, 3, 2]]
