from collections import defaultdict

from aoc.utils import read_lines

# Input data
connections = read_lines("day23/example.txt")

# Step 1: Parse the input to create a graph representation
graph = defaultdict(set)
for connection in connections:
    a, b = connection.split("-")
    graph[a].add(b)
    graph[b].add(a)

# Step 2: Find all triangles in the graph
triangles = set()
for a in graph:
    for b in graph[a]:
        for c in graph[b]:
            if c in graph[a] and a < b < c:  # Ensure unique and sorted order
                triangles.add((a, b, c))

# Step 3: Filter triangles to include only those with at least one computer name starting with 't'
triangles_with_t = [triangle for triangle in triangles if any(node.startswith("t") for node in triangle)]

# Output the result
print(f"Total triangles: {len(triangles)}")
print(f"Triangles with at least one 't': {len(triangles_with_t)}")
print("Triangles with 't':", triangles_with_t)
