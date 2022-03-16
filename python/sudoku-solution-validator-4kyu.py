def valid_solution(board):
#     Check rows and columns
    for row_i ,row in enumerate(board):
        column = []
        for col_i, y in enumerate(board):
            column.append(board[col_i][row_i])
        for num in range(1,9):
            if column.count(num) > 1:
                return False
            if row.count(num) > 1:
                return False
#     Check Grids
    grids = []
    for x in range(0,9):
        grid = []
        for y in range(0,3):
            for i in range(0,3):
                grid.append(board[y][i])
        grids.append(grid)

    for grid in grids:
        if sorted(grid) != list(range(1,10)):
            return False
        
    return True