class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stepsToTgt = key=lambda x: math.ceil(target-x[0])/x[1]
        sortedCars = sorted(zip(position, speed), key=lambda x: -x[0])
        lastFleet = 0
        fleets = 1
        for i in range(1, len(sortedCars)):
            if stepsToTgt(sortedCars[i]) > stepsToTgt(sortedCars[lastFleet]):
                fleets += 1
                lastFleet = i
        return fleets