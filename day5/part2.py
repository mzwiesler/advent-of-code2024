from collections import defaultdict
from typing import Dict, List, Set, Tuple


def parse_input(content: str) -> Tuple[List[str], List[List[int]]]:
    sections = content.strip().split("\n\n")
    rules = sections[0].split("\n")
    updates = [list(map(int, update.split(","))) for update in sections[1].split("\n")]
    return rules, updates


def build_graph(rules: List[str]) -> Dict[int, List[int]]:
    graph = defaultdict(list)
    for rule in rules:
        x, y = map(int, rule.split("|"))
        graph[x].append(y)
    return graph


def is_correct_order(update, graph: Dict[int, List[int]]) -> bool:
    this_update = update.copy()
    while this_update:
        node = this_update.pop()
        for neighbor in graph[node]:
            if neighbor in this_update:
                return False
    return True


def dfs(node: int, graph: Dict[int, List[int]], visited: Set[int], stack: List[int], update_set: Set[int]) -> None:
    """
    Perform a Depth-First Search (DFS) on a graph starting from a given node.

    Args:
        node (int): The starting node for the DFS.
        graph (Dict[int, List[int]]): The adjacency list representation of the graph.
        visited (Set[int]): A set to keep track of visited nodes.
        stack (List[int]): A list to store the nodes in the order they are finished.
        update_set (Set[int]): A set of nodes that need to be updated during the DFS.

    Returns:
        None
    """
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor in update_set and neighbor not in visited:
            dfs(neighbor, graph, visited, stack, update_set)
    stack.append(node)


def topological_sort_dfs(update: List[int], graph: Dict[int, List[int]]):
    """
    Perform a topological sort on a directed graph using Depth-First Search (DFS).
    Args:
        update (List[int]): A list of nodes to be updated.
        graph (Dict[int, List[int]]): A dictionary representing the adjacency list of the graph,
                                      where keys are node identifiers and values are lists of adjacent nodes.
    Returns:
        List[int]: A list of nodes in topologically sorted order.
    """

    visited = set()
    stack = []
    update_set = set(update)

    for node in update:
        if node not in visited:
            dfs(node, graph, visited, stack, update_set)

    stack.reverse()  # Reverse the stack to get the correct topological order
    return stack


def find_middle_page(update: List[int]) -> int:
    return update[len(update) // 2]


def read_file_as_string(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
    return content


def main(path: str) -> int:
    content = read_file_as_string(path)
    rules, updates = parse_input(content)
    graph = build_graph(rules)

    total_middle_sum = 0
    for update in updates:
        if not is_correct_order(update, graph):
            sorted_update = topological_sort_dfs(update, graph)
            total_middle_sum += find_middle_page(sorted_update)

    return total_middle_sum


if __name__ == "__main__":
    input_sum_example = main(path="day5/example.txt")
    assert input_sum_example == 123
    input_sum_input = main(path="day5/input.txt")
    print(str(input_sum_input))
