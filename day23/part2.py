from collections import defaultdict

from aoc.utils import read_lines

# Input data
connections = read_lines("day23/input.txt")

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split("-")
    graph[a].add(b)
    graph[b].add(a)


def connect(node: str, connected: set[str], graph: dict[str, set[str]], parties: set[str]) -> set[str]:
    party = ",".join(sorted(connected))
    if party in parties:
        return parties
    parties.add(party)
    for neighbor in graph[node]:
        if neighbor in connected:
            continue
        if not all(neighbor in graph[con_node] for con_node in connected):
            continue
        connected.add(neighbor)
        parties = connect(neighbor, connected, graph, parties)
    return parties


parties = set()
for node in graph:
    parties.update(connect(node, {node}, graph, parties))

print(max(parties, key=len))
