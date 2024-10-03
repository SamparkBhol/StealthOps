import heapq

class Node:
    """Represents a point in the grid for pathfinding."""
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0  # Cost from start to node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node, goal):
    """Manhattan distance heuristic for grid-based pathfinding."""
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def a_star_pathfinding(start, goal, grid):
    """A* pathfinding algorithm."""
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, start))

    while open_list:
        current = heapq.heappop(open_list)[1]

        # Goal reached
        if current.x == goal.x and current.y == goal.y:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]

        closed_list.add((current.x, current.y))

        # Check neighbors (4 directions: up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_x, neighbor_y = current.x + dx, current.y + dy

            # Ignore if out of bounds or blocked
            if not (0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0])):
                continue
            if grid[neighbor_x][neighbor_y] == 1:  # Blocked
                continue

            neighbor = Node(neighbor_x, neighbor_y, current)

            if (neighbor.x, neighbor.y) in closed_list:
                continue

            neighbor.g = current.g + 1
            neighbor.h = heuristic(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h

            heapq.heappush(open_list, (neighbor.f, neighbor))

    return None  # No path found

def print_path(path):
    """Utility to print path coordinates."""
    if path:
        print("Path found:")
        for point in path:
            print(point)
    else:
        print("No path found.")

if __name__ == "__main__":
    # Example grid (0 = walkable, 1 = blocked)
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ]

    start = Node(0, 0)
    goal = Node(4, 4)
    path = a_star_pathfinding(start, goal, grid)
    print_path(path)