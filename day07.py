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
    lowest = 999999999
    for alignPoint in range(minX, maxX):
        fuelConsumption = []
        print(f"Day07b: ({lowest:,}) {round(100*alignPoint/(maxX-minX),1)}%", end="\r")
        for i, x in enumerate(data):
            fuelConsumption.append(0)
            distance = abs(alignPoint - x)
            for step in range(distance):
                fuelConsumption[i] += step + 1
        total = sum(fuelConsumption)
        if total < lowest:
            lowest = total
    return lowest


print(f"Day07a: {leastFuel(data)}")  # 337833
print(f"Day07b: {leastFuelWithResistance(data)}")  # 96678050
