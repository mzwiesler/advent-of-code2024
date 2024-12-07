from collections import defaultdict


def parse_input(content):
    sections = content.strip().split("\n\n")
    rules = sections[0].split("\n")
    updates = [list(map(int, update.split(","))) for update in sections[1].split("\n")]
    return rules, updates


def build_graph(rules):
    graph = defaultdict(list)
    for rule in rules:
        x, y = map(int, rule.split("|"))
        graph[x].append(y)

    return graph


def is_correct_order(update, graph):
    this_update = update.copy()
    while this_update:
        node = this_update.pop()
        for neighbor in graph[node]:
            if neighbor in this_update:
                return False
    return True


def find_middle_page(update):
    return update[len(update) // 2]


def read_file_as_string(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content


def main(path):
    content = read_file_as_string(path)
    rules, updates = parse_input(content)
    graph = build_graph(rules)

    total_middle_sum = 0
    for update in updates:
        if is_correct_order(update, graph):
            total_middle_sum += find_middle_page(update)

    return total_middle_sum


if __name__ == "__main__":
    input_sum_example = main(path="day5/example.txt")
    assert input_sum_example == 143
    input_sum_input = main(path="day5/input.txt")
    print(str(input_sum_input))
