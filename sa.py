import math
import random

def aneal(cords):
    coordinates = cords
    N = len(coordinates)
    temp = math.sqrt(N)  # temperature of the algorithm. can start with any number
    iterations = 100000
    alpha = 0.995  # every iteration the temp is changing by alpha.
    stopping_temp = 1e-8  # temp is not stopping at 0 to prevent underflow
    firstSolution = greedySolution(N, coordinates)
    firstDist = calculateSolutionDist(firstSolution)
    iteration = 1
    currentSol = firstSolution.copy()
    currentDist = firstDist
    bestSol = firstSolution.copy()
    bestDist = firstDist
    while temp >= stopping_temp and iteration <= iterations:
      temp *= alpha
      iteration += 1
      values = random.randint(2, N - 1)  # how many values will be reversed
      startingIndex = random.randint(0, N - values)
      newSol = currentSol.copy()
      newSol[startingIndex: (startingIndex + values)] = reversed(currentSol[startingIndex: (startingIndex + values)])
      newSolDist = calculateSolutionDist(newSol)
      if newSolDist < currentDist:
          currentSol = newSol.copy()
          currentDist = newSolDist
          if newSolDist < bestDist:
              bestDist = newSolDist
              bestSol = newSol.copy()
      else:
          if random.random() < p_accept(temp, newSolDist, currentDist):
              currentSol = newSol.copy()
              currentDist = newSolDist
    print("Best distance: ", bestDist)
    improvement = 100 * (firstDist - bestDist) / firstDist
    print(f"Improvement over greedy heuristic: {improvement : .2f}%")


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def greedySolution(N, coordinates):
    remainingIndexs = set(range(0, N))
    first = random.randint(0, N - 1)
    remainingIndexs.remove(first)
    solution = [coordinates[first]]
    # remaining = set(self.coordinates)
    # remaining.remove(self.coordinates[first])
    current = coordinates[first]
    while (len(remainingIndexs) != 0):
        mindist = float("inf")
        nextNode = None
        minIndex = 0
        for i in remainingIndexs:
            x = coordinates[i]
            myDist = dist(current, x)
            if (myDist < mindist):
                mindist = myDist
                nextNode = x
                minIndex = i
        solution.append(nextNode)
        current = nextNode
        remainingIndexs.remove(minIndex)
        # remaining.remove(nextNode)
    return solution

def calculateSolutionDist(solution):
    totalDist = 0
    for i in range(len(solution)):
        if (i == len(solution) - 1):
            totalDist += dist(solution[i], solution[0])
            break
        p1 = solution[i]
        p2 = solution[i + 1]
        totalDist += dist(p1, p2)
    return totalDist

def p_accept(temp, newDist, currentDist):
    return math.exp(-abs(newDist - currentDist) / temp)


