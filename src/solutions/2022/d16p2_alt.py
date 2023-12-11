import itertools

from utils import run, ParsingConfig, Example

example_answer = 1707

example_data = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""


def parse(*args):
    valve_name = args[1]
    flow_rate = int(args[4].split("=")[1].split(";")[0])
    neighbours = [arg.replace(",", "") for arg in args[9:]]
    return valve_name, flow_rate, neighbours


parsing_config = ParsingConfig(
    parser_func=parse,
)


def find_distances(names, neighbours):
    distances = {(name, other): 1 for name, others in neighbours.items() for other in others}
    queue = [list(key) for key in distances]
    while queue:
        current = queue.pop()
        for neighbour in neighbours[current[-1]]:
            key = (current[0], neighbour)
            distance = len(current)
            if key not in distances or distances[key] > distance:
                distances[key] = distance
                queue.append(current + [neighbour])
    output = {name: {} for name in names}
    for (d1, d2), distance in distances.items():
        if d1 in names and d2 in names:
            output[d1][d2] = distance
    return output


def solve(data):
    flow_rates = {name: flow_rate for name, flow_rate, _ in data}
    nonzero_flow_rates = [name for name, flow_rate, _ in data if flow_rate > 0]
    neighbours = {name: _neighbours for name, _, _neighbours in data}
    distances = find_distances(nonzero_flow_rates + ["AA"], neighbours)
    best = 0

    midpoint = len(nonzero_flow_rates) // 2
    for length in range(midpoint):
        for el_subset in itertools.combinations(nonzero_flow_rates, midpoint - length):
            el_distances = {name: {other: distance for other, distance in others.items() if other in el_subset} for name, others in distances.items() if name in el_subset or name == "AA"}
            my_distances = {name: {other: distance for other, distance in others.items() if other not in el_subset} for name, others in distances.items() if name not in el_subset}

            queue = [("AA", 26, 0, [])]
            subset_best = 0
            while queue:
                name, time_remaining, score, open_valves = queue.pop(0)

                for other, distance in my_distances[name].items():
                    if other not in open_valves and time_remaining > distance + 1:
                        new_time = time_remaining - distance - 1
                        new_score = score + (new_time * flow_rates[other])
                        new_open_valves = open_valves + [other]

                        if new_score > subset_best:
                            subset_best = new_score
                        else:
                            theoretical_max_subset_score = new_score + sum(
                                flow_rates[other2] * max(0, (new_time - other_distance - 1))
                                for other2, other_distance in my_distances[other].items()
                                if other2 not in new_open_valves
                            )
                            if theoretical_max_subset_score < subset_best:
                                continue
                            theoretical_max_score = theoretical_max_subset_score + sum(
                                flow_rates[other2] * 26
                                for other2, other_distance in el_distances["AA"].items()
                            )
                            if theoretical_max_score < best:
                                continue

                        new_state = (other, new_time, new_score, new_open_valves)
                        queue.append(new_state)

            queue = [("AA", 26, subset_best, [])]
            while queue:
                name, time_remaining, score, open_valves = queue.pop(0)

                for other, distance in el_distances[name].items():
                    if other not in open_valves and time_remaining > distance + 1:
                        new_time = time_remaining - distance - 1
                        new_score = score + (new_time * flow_rates[other])
                        new_open_valves = open_valves + [other]

                        if new_score > best:
                            best = new_score
                            print("New best!", best, new_open_valves, "Queue size:", len(queue))
                        else:
                            theoretical_max_score = new_score + sum(
                                flow_rates[other2] * max(0, (new_time - other_distance - 1))
                                for other2, other_distance in el_distances[other].items()
                                if other2 not in new_open_valves
                            )
                            if theoretical_max_score < best:
                                continue

                        new_state = (other, new_time, new_score, new_open_valves)
                        queue.append(new_state)

    return best


real_answer = 2775


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
