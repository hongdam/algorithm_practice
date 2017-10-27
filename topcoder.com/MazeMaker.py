class MazeMaker:
    def longestPath(self, maze, startRow, startCol, moveRow, moveCol):

        # result_cost = [[0]*len(maze[0]) for _ in range(len(maze))]

        result_cost = [[-1 if x == '.' else 'X' for x in y] for y in maze]

        queue = [[startRow, startCol]]
        result_cost[startRow][startCol] = 0

        while queue:
            c_row, c_col = queue.pop(0)

            for m_r, m_c in zip(moveRow, moveCol):

                next_r, next_c = c_row + m_r, c_col + m_c

                if 0 <= next_r < len(maze) and \
                        0 <= next_c < len(maze[0]) and \
                        result_cost[next_r][next_c] == -1 and \
                        maze[next_r][next_c] == '.':

                    result_cost[next_r][next_c] = result_cost[c_row][c_col] + 1

                    queue.append([next_r, next_c])

        flatten_r = sum(result_cost, [])
        flatten_r = [x for x in flatten_r if x != 'X']

        return -1 if min(flatten_r) == -1 else max(flatten_r)


s = MazeMaker()
maze = ["X.X", "...", "XXX", "X.X"]
startRow = 0
startCol = 1
moveRow = [1, 0, -1, 0]
moveCol = [0, 1, 0, -1]
print(s.longestPath(maze, startRow, startCol, moveRow, moveCol))