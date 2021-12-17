def ingestInput(data):
    # In: '0,9 -> 5,9'
    # Out: [[0,9,5,9]]
    instructions = []
    newline = []
    for line in data:
        points = line.split(" -> ")
        for item in points:
            pointpoint = item.split(",")
            for p in pointpoint:
                newline.append(int(p.strip()))
        instructions.append(newline)
        newline = []
    return instructions


def fieldSize(instructions):
    xmin = 9999999
    xmax = 0
    ymin = 9999999
    ymax = 0
    for instruction in instructions:
        x1, y1, x2, y2 = instruction
        if min(x1, x2) < xmin:
            xmin = min(x1, x2)
        if min(y1, y2) < ymin:
            ymin = min(y1, y2)
        if max(x1, x2) > xmax:
            xmax = max(x1, x2)
        if max(y1, y2) > ymax:
            ymax = max(y1, y2)
    return (1 + xmax, 1 + ymax)


def constructEmptyField(xsize, ysize):
    emptyField = []
    for y in range(0, ysize):
        row = []
        for x in range(0, xsize):
            row.append(0)
        emptyField.append(row)
    return emptyField


def fieldFromInstructions(instructions):
    xrange, yrange = fieldSize(instructions)
    field = constructEmptyField(xrange, yrange)
    for instruction in instructions:
        x1, y1, x2, y2 = instruction
        if x1 == x2:
            # sort y values ascending
            if y1 > y2:
                y1, y2 = y2, y1
            # insert into field
            for y in range(y1, y2 + 1):
                field[y][x1] += 1
        elif y1 == y2:
            # sort x values ascending
            if x1 > x2:
                x1, x2 = x2, x1
            # insert into field
            for x in range(x1, x2 + 1):
                field[y1][x] += 1
    return field


def fieldFromInstructionsWithDiagonals(instructions):
    xrange, yrange = fieldSize(instructions)
    field = constructEmptyField(xrange, yrange)
    for instruction in instructions:
        x1, y1, x2, y2 = instruction
        if x1 == x2:
            # sort y values ascending
            if y1 > y2:
                y1, y2 = y2, y1
            # insert into field
            for y in range(y1, y2 + 1):
                field[y][x1] += 1
        elif y1 == y2:
            # sort x values ascending
            if x1 > x2:
                x1, x2 = x2, x1
            # insert into field
            for x in range(x1, x2 + 1):
                field[y1][x] += 1
        else:
            # conditionally sort the points so we only have to go right-up or right-down
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            for i in range(0, x2 - x1 + 1):
                if y1 < y2:
                    field[y1 + i][x1 + i] += 1
                if y1 > y2:
                    field[y1 - i][x1 + i] += 1
    return field


# At how many points do at least two lines overlap?
def countDoublePlusPoints(field):
    count = 0
    for row in field:
        for x in row:
            if x > 1:
                count += 1
    return count


def analyseInputForDoublePoints(data):
    instructions = ingestInput(data)
    fieldLayout = fieldFromInstructions(instructions)
    return countDoublePlusPoints(fieldLayout)


def analyseInputForDoublePointsWithDiagonals(data):
    instructions = ingestInput(data)
    fieldLayout = fieldFromInstructionsWithDiagonals(instructions)
    return countDoublePlusPoints(fieldLayout)


with open("day05-input.txt", "r") as f:
    data = f.readlines()

if __name__ == "__main__":
    print(f"Day05a: {analyseInputForDoublePoints(data)}")  # 5306
    print(f"Day05b: {analyseInputForDoublePointsWithDiagonals(data)}")  # 17787
