from collections import defaultdict


def parse_file(input_file):
    with open(input_file) as f:
        next_dict = defaultdict(dict)
        nodes_count = int(f.readline().strip('\n'))
        for i in range(nodes_count):
            next_nodes = f.readline().split()
            for n in range(0, len(next_nodes), 2):
                if next_nodes[n] == '0':
                    break
                next_dict[i+1].update({int(next_nodes[n]): int(next_nodes[n+1])})
        start = int(f.readline().strip('\n'))
        finish = int(f.readline().strip('\n'))
        return next_dict, start, finish, nodes_count


def dijkstra(input_file):
    parsed = parse_file(input_file)
    next_dict = parsed[0]
    start = parsed[1]
    finish = parsed[2]
    count = parsed[3]
    visited = {start: 0}
    path = {}
    nodes = [i+1 for i in range(count)]
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]
        for next_node, next_weight in next_dict[min_node].items():
            weight = current_weight + next_weight
            if next_node not in visited or weight < visited[next_node]:
                visited[next_node] = weight
                path[next_node] = min_node

    result = make_result(path, start, finish) if finish in path else []
    weight = visited[finish] if result else 0
    write_file('out.txt', result, weight)


def make_result(path, start, finish):
    result = []
    current_node = finish
    while current_node != start:
        result.append(current_node)
        current_node = path[current_node]
    result.append(start)
    result.reverse()
    return result


def write_file(out_file, result, weight):
    with open(out_file, 'w') as f:
        if result:
            f.writelines(['Y\n', ' '.join([str(x) for x in result]) + '\n', str(weight)])
        else:
            f.write('N')


dijkstra('in.txt')
