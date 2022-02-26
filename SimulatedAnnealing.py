import math
import random


def simulate(cords):
    coordinates = cords
    N = len(coordinates)
    temp = math.sqrt(N)  # temperature of the algorithm. can start with any number
    iterations = 100000
    alpha = 0.995  # every iteration the temp is changing by alpha.
    stopping_temp = 1e-8  # temp is not stopping at 0 to prevent underflow
    firstSolution = greedySolution(N, coordinates)
    firstDist = calculate_solution_dist(firstSolution)
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
        newSolDist = calculate_solution_dist(newSol)
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
    remaining_indexs = set(range(0, N))
    first = random.randint(0, N - 1)
    remaining_indexs.remove(first)
    solution = [coordinates[first]]
    # remaining = set(self.coordinates)
    # remaining.remove(self.coordinates[first])
    current = coordinates[first]
    while len(remaining_indexs) != 0:
        min_distance = float("inf")
        next_node = None
        min_index = 0
        for i in remaining_indexs:
            x = coordinates[i]
            my_distance = dist(current, x)
            if my_distance < min_distance:
                min_distance = my_distance
                next_node = x
                min_index = i
        solution.append(next_node)
        current = next_node
        remaining_indexs.remove(min_index)
        # remaining.remove(next_node)
    return solution


def calculate_solution_dist(solution):
    total_distance = 0
    for i in range(len(solution)):
        if i == len(solution) - 1:
            total_distance += dist(solution[i], solution[0])
            break
        p1 = solution[i]
        p2 = solution[i + 1]
        total_distance += dist(p1, p2)
    return total_distance


def p_accept(temp, new_distance, current_distance):
    return math.exp(-abs(new_distance - current_distance) / temp)
