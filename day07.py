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


def leastFuelWithResistance(data):
    minX = min(data)
    maxX = max(data)
    lowest = 9999999999
    for alignPoint in range(minX, maxX):
        fuelConsumption = 0
        for x in data:
            distance = abs(alignPoint - x)
            fuelConsumption += int(distance * (distance + 1) / 2)
        if fuelConsumption < lowest:
            lowest = fuelConsumption
    return lowest


if __name__ == "__main__":
    print(f"Day07a: {leastFuel(data)}")  # 337833
    print(f"Day07b: {leastFuelWithResistance(data)}")  # 96678050
