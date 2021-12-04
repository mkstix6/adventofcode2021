with open("day02.txt", "r") as f:
    data = f.readlines()


def submarineDestination(data):
    # setup
    position = {"horizontal": 0, "depth": 0}
    # process data
    for line in data:
        instruction, value = line.split(" ")
        value = int(value)
        if instruction == "forward":
            position["horizontal"] += value
        if instruction == "up":
            position["depth"] -= value
        if instruction == "down":
            position["depth"] += value
    # result
    return position


print(
    f"Day02a: {submarineDestination(data)['horizontal'] * submarineDestination(data)['depth']}"
)
