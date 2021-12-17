# fmt:off
exampleInput = [3,4,3,1,2]
input = [1,1,1,2,1,5,1,1,2,1,4,1,4,1,1,1,1,1,1,4,1,1,1,1,4,1,1,5,1,3,1,2,1,1,1,2,1,1,1,4,1,1,3,1,5,1,1,1,1,3,5,5,2,1,1,1,2,1,1,1,1,1,1,1,1,5,4,1,1,1,1,1,3,1,1,2,4,4,1,1,1,1,1,1,3,1,1,1,1,5,1,3,1,5,1,2,1,1,5,1,1,1,5,3,3,1,4,1,3,1,3,1,1,1,1,3,1,4,1,1,1,1,1,2,1,1,1,4,2,1,1,5,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,5,1,1,1,1,3,1,1,1,1,1,3,4,1,2,1,3,2,1,1,2,1,1,1,1,4,1,1,1,1,4,1,1,1,1,1,2,1,1,4,1,1,1,5,3,2,2,1,1,3,1,5,1,5,1,1,1,1,1,5,1,4,1,2,1,1,1,1,2,1,3,1,1,1,1,1,1,2,1,1,1,3,1,4,3,1,4,1,3,2,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,2,1,5,1,1,1,1,2,1,1,1,3,5,1,1,1,1,5,1,1,2,1,2,4,2,2,1,1,1,5,2,1,1,5,1,1,1,1,5,1,1,1,2,1]
# fmt:on


class FishSim:
    def __init__(self, startState) -> None:
        self.fishState = startState.copy()

    def runSim(self, steps):
        for _ in range(steps):
            for index, f in enumerate(self.fishState):
                if f == 0:
                    self.fishState.append(9)
                    self.fishState[index] += 6
                else:
                    self.fishState[index] -= 1
        self.totalFish = len(self.fishState)
        return True


class BigFishSim:
    def __init__(self, startState) -> None:
        # count fish of identical countdowns
        counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in startState:
            counts[x] += 1
        self.counts = counts

    def runSim(self, steps):
        for _ in range(steps):
            newCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(len(newCount)):
                if i == 0:
                    newCount[6] += self.counts[0]
                    newCount[8] += self.counts[0]
                else:
                    newCount[i - 1] += self.counts[i]
            self.counts = newCount

    def totalFish(self):
        return sum(self.counts)


fishies = FishSim(input)
fishies.runSim(80)

fishies256 = BigFishSim(input)
fishies256.runSim(256)

if __name__ == "__main__":
    # fmt:off
    print(f"Day06a: {fishies.totalFish}")  # 391671 # confirmed answer for day06a
    print(f"Day06b: {fishies256.totalFish()}")  # 1754000560399 # confirmed answer for day06b
    # fmt:on
