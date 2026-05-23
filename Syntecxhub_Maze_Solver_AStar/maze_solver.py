import heapq

# Directions: Up, Down, Left, Right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Heuristic Function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* Search Algorithm
def astar(maze, start, goal):

    rows = len(maze)
    cols = len(maze[0])

    # Priority Queue
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}

    g_cost = {start: 0}

    f_cost = {start: heuristic(start, goal)}

    visited = set()

    while open_list:

        current = heapq.heappop(open_list)[1]

        # Goal Reached
        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        visited.add(current)

        for dx, dy in DIRECTIONS:

            neighbor = (current[0] + dx, current[1] + dy)

            x, y = neighbor

            # Check boundaries
            if x < 0 or x >= rows or y < 0 or y >= cols:
                continue

            # Check wall
            if maze[x][y] == 1:
                continue

            tentative_g = g_cost[current] + 1

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:

                came_from[neighbor] = current
                g_cost[neighbor] = tentative_g

                f = tentative_g + heuristic(neighbor, goal)
                f_cost[neighbor] = f

                if neighbor not in visited:
                    heapq.heappush(open_list, (f, neighbor))

    return None


# Print Maze with Path
def print_maze(maze, path, start, goal):

    maze_copy = [row[:] for row in maze]

    for x, y in path:
        if (x, y) != start and (x, y) != goal:
            maze_copy[x][y] = "*"

    for i in range(len(maze_copy)):
        for j in range(len(maze_copy[0])):

            if (i, j) == start:
                print("S", end=" ")

            elif (i, j) == goal:
                print("G", end=" ")

            elif maze_copy[i][j] == 1:
                print("#", end=" ")

            elif maze_copy[i][j] == "*":
                print("*", end=" ")

            else:
                print(".", end=" ")

        print()


# Main Program
maze = [
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 5)

path = astar(maze, start, goal)

if path:
    print("Shortest Path Found:")
    print(path)

    print("\nMaze Visualization:\n")
    print_maze(maze, path, start, goal)

else:
    print("No path found!")