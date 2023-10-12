from queue import Queue

# Define the maze as a list of lists
maze = [
    ['#', '#', '#', '#', '#', '#'],
    ['#', 'S', '#', '#', ' ', '#'],
    ['#', '', '# ', '#', ' ', '#'],
    ['#', '', 'G', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', '#'],
    ['#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#']
]

# Define the start and goal positions
start = (1, 1)
goal = (3, 2)

# Define the possible moves
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# BFS algorithm
def bfs(maze, start, goal):
    queue = Queue()
    queue.put([start])
    visited = set()

    while not queue.empty():
        path = queue.get()
        position = path[-1]

        if position == goal:
            return path  # Return the path as a list of positions

        for move in moves:
            new_position = (position[0] + move[0], position[1] + move[1])

            if (
                0 <= new_position[0] < len(maze) and
                0 <= new_position[1] < len(maze[0]) and
                maze[new_position[0]][new_position[1]] != '#' and
                new_position not in visited
            ):
                new_path = path.copy()
                new_path.append(new_position)
                queue.put(new_path)
                visited.add(new_position)

    return []  # If no path is found, return an empty list

# Find and print the possible routes
route = bfs(maze, start, goal)

if not route:
    print("No path found.")
else:
    print("Route:")
    for position in route:
        x, y = position
        maze[x][y] = 'X'  # Mark the path with 'X'
    maze[start[0]][start[1]] = 'S'
    maze[goal[0]][goal[1]] = 'G'

    for row in maze:
        print(' '.join(row))