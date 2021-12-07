with open("day07-input.txt", "r") as f:
    data = f.readlines()
data = [int(x) for x in data[0].split(",")]


def leastFuel(data):
    minX = min(data)
    maxX = max(data)

    iterations = []
    for alignPoint in range(minX, maxX):
        fuelConsumption = []
        for x in data:
            fuelConsumption.append(abs(alignPoint - x))
        iterations.append(fuelConsumption)

    totals = [sum(iteration) for iteration in iterations]
    lowest = min(totals)
    return lowest


print(f"Day07a: {leastFuel(data)}")  # 337833
# print(f"Day07b: {leastFuel(data)}")  # ???
