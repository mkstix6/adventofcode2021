with open("day02-input.txt", "r") as f:
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


def submarineDestinationWithAim(data):
    # setup
    position = {"horizontal": 0, "depth": 0}
    aim = 0
    # process data
    for line in data:
        instruction, value = line.split(" ")
        value = int(value)
        if instruction == "forward":
            position["horizontal"] += value
            position["depth"] += value * aim
        if instruction == "up":
            aim -= value
        if instruction == "down":
            aim += value
    # result
    return position


if __name__ == "__main__":
    print(
        f"Day02a: {submarineDestination(data)['horizontal'] * submarineDestination(data)['depth']}"
    )
    print(
        f"Day02b: {submarineDestinationWithAim(data)['horizontal'] * submarineDestinationWithAim(data)['depth']}"
    )
