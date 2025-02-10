import json
import sys

def find_cheapest_price(n, flights, src, dst, k):
    graph = {}
    for u, v, w in flights:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    queue = [(0, src, 0)]
    min_cost = {(src, 0): 0}

    while queue:
        cost, city, stops = queue.pop(0)

        if city == dst:
            continue

        if stops <= k:
            for neighbor, price in graph.get(city, []):
                new_cost = cost + price

                if (neighbor, stops + 1) not in min_cost or new_cost < min_cost[(neighbor, stops + 1)]:
                    min_cost[(neighbor, stops + 1)] = new_cost
                    queue.append((new_cost, neighbor, stops + 1))

    result = min([min_cost[(dst, s)] for s in range(k + 2) if (dst, s) in min_cost], default=-1)
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python cheapest_flight_finder.py <input_file.json>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            data = json.load(file)

        n = data['n']
        flights = data['flights']
        src = data['src']
        dst = data['dst']
        k = data['k']

        result = find_cheapest_price(n, flights, src, dst, k)
        print(f"The cheapest price from city {src} to city {dst} with at most {k} stops is: {result}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{input_file}' contains invalid JSON.")
    except KeyError as e:
        print(f"Error: Missing key in input JSON - {e}")

if __name__ == "__main__":
    main()
