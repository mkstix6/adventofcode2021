# Define custom types
CoordinateType = tuple[int, int]
CoordinateListType = list[CoordinateType]
InstructionType = tuple[str, int]
InstructionListType = list[InstructionType]
# Constants

# Import file
with open("day13-input.txt", "r") as f:
    data = f.read()
# Format data


def toCoordinates(line: str) -> CoordinateType:
    x, y = line.split(",")
    return int(x), int(y)


def toInstructions(line: str) -> InstructionType:
    foldDirection, foldIndex = line.split(" ")[2].split("=")
    return foldDirection, int(foldIndex)


def processInput(data) -> tuple[CoordinateListType, InstructionListType]:
    part1, part2 = data.split("\n\n")
    coordinates: CoordinateListType = list(map((toCoordinates), part1.split("\n")))
    instructions: InstructionListType = list(map(toInstructions, part2.split("\n")))
    return coordinates, instructions


def fold(
    coordinates: CoordinateListType, instruction: InstructionType
) -> CoordinateListType:

    return 1


def countDots(coordinates: CoordinateListType) -> int:
    return 1


def day13a(data):
    coordinates, instructions = processInput(data)
    firstFold = fold(coordinates, instructions[0])
    count = countDots(firstFold)
    return 1


def day13b(data):
    return 1


if __name__ == "__main__":
    # How many dots are visible after completing just the first fold instruction on your transparent paper?
    print(f"Day13a: {day13a(data)}")  # ???
    # ???
    print(f"Day13b: {day13b(data)}")  # ???
