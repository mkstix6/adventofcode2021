# Import file
with open("day11-input.txt", "r") as f:
    data = f.readlines()
# Format data
data = [[int(y) for y in x.strip()] for x in data]

neighbours = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def gridHasCharged(grid) -> bool:
    flat = [item for row in grid for item in row if item > 9]
    return len(flat) > 0


def step(grid: list[list[int]]) -> tuple[list[list[int]], int]:
    grid = grid.copy()
    flashCount = 0
    # Increase all by 1
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1
    # Simulate flashes
    while gridHasCharged(grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 9:
                    grid[y][x] = -99
                    flashCount += 1
                    for (dx, dy) in neighbours:
                        try:
                            if y + dy >= 0 and x + dx >= 0:
                                grid[y + dy][x + dx] += 1
                        except IndexError:
                            pass  # ...
    # Set flashes to zero
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] < 0:
                grid[y][x] = 0
    return grid, flashCount


def day11a(grid: list[list[int]]) -> int:
    doSteps = 100
    flashCount = 0
    for i in range(doSteps):
        grid, newFlashes = step(grid)
        flashCount += newFlashes

    return flashCount


if __name__ == "__main__":
    # How many total flashes are there after 110 steps?
    print(f"Day11a: {day11a(data)}")  # ???
    # ???
    # print(f"Day11b: {day11b(data)}")  # ???
