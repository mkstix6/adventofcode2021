# Define custom types
InputDataType = list[str]
EdgesType = set[tuple[str, str]]
NodesType = set[str]

# Constants
startPoint = "start"
endPoint = "end"

# Import file
with open("day12-input.txt", "r") as f:
    data: InputDataType = f.readlines()
# Format data
data: InputDataType = [x for x in data]


def processData(data: InputDataType) -> tuple[EdgesType, NodesType]:
    edges: EdgesType = set(
        [tuple(sorted(row.strip().split("-"), key=str.casefold)) for row in data]
    )
    nodes: NodesType = set([pair for row in data for pair in row.strip().split("-")])
    return edges, nodes


def nodeConnections(
    node: str, edges: set[tuple[str, str]], nodes: NodesType, used: list[str]
) -> set[str]:
    connections = {x for x in edges if node in x}
    neighbours = [[x for x in pair if x != node][0] for pair in connections]
    return set(neighbours)


def nextStep(fromNode, edges, nodes, routes, used):
    for toNode in nodeConnections(fromNode, edges, nodes, used):
        usedCopy = used.copy()
        # Abort if next destination is invalid
        if toNode in usedCopy and isSmallCave(toNode):
            continue
        # Add the destination to the route
        usedCopy.append(toNode)
        # Check for end condition
        if toNode == endPoint:
            routes.append(usedCopy)
            continue
        # Look further into the solution
        else:
            nextStep(toNode, edges, nodes, routes, usedCopy)


def isSmallCave(node: str):
    return node == node.lower()


def day12a(data: InputDataType) -> int:
    routes = []
    # Start at start
    edges, nodes = processData(data)
    # Each step
    used = [startPoint]
    nextStep(startPoint, edges, nodes, routes, used)
    return len(routes)


def day12b(edges: InputDataType) -> int:
    return 1


if __name__ == "__main__":
    # How many paths through this cave system are there that visit small caves at most once?
    print(f"Day12a: {day12a(data)}")  # ???
    # ???
    print(f"Day12b: {day12b(data)}")  # ???
