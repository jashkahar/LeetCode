class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        original_rows, original_cols = len(grid), len(grid[0])
        expanded_rows, expanded_cols = 3 * original_rows, 3 * original_cols
        expanded_grid = [[0] * expanded_cols for _ in range(expanded_rows)]

        for row in range(original_rows):
            for col in range(original_cols):
                expanded_row, expanded_col = row * 3, col * 3
                if grid[row][col] == "/":
                    expanded_grid[expanded_row][expanded_col + 2] = 1
                    expanded_grid[expanded_row + 1][expanded_col + 1] = 1
                    expanded_grid[expanded_row + 2][expanded_col] = 1
                elif grid[row][col] == "\\":
                    expanded_grid[expanded_row][expanded_col] = 1
                    expanded_grid[expanded_row + 1][expanded_col + 1] = 1
                    expanded_grid[expanded_row + 2][expanded_col + 2] = 1

        def dfs(current_row, current_col, visited_cells):
            if (current_row < 0 or current_col < 0 or 
                current_row >= expanded_rows or current_col >= expanded_cols or 
                expanded_grid[current_row][current_col] != 0 or 
                (current_row, current_col) in visited_cells):
                return
            visited_cells.add((current_row, current_col))
            directions = [(current_row + 1, current_col), (current_row, current_col + 1),
                          (current_row - 1, current_col), (current_row, current_col - 1)]
            
            for next_row, next_col in directions:
                dfs(next_row, next_col, visited_cells)

        visited_cells = set()
        regions_count = 0
        for row in range(expanded_rows):
            for col in range(expanded_cols):
                if expanded_grid[row][col] == 0 and (row, col) not in visited_cells:
                    dfs(row, col, visited_cells)
                    regions_count += 1

        return regions_count
