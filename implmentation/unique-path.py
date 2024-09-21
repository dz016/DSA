def most_profitable_path(grid):
    if not grid or not grid[0]:
        return 0

    dp=[[-1] *len(grid[i]) for i in range(len(grid)) ]
    dp[0][0] = grid[0][0]
    for i in range(0,len(grid)):
        for j in range(0, len(grid[i])):
            if i ==0 and j ==0:
                continue
            elif j ==0:
                dp[i][j] = grid[i][j] + dp[i-1][j]
            elif i == 0:
                dp[i][j] = grid[i][j] + dp[i][j-1]
            else:
                dp[i][j]=  max(dp[i][j-1] , dp[i-1][j] ) + grid[i][j]

    print(dp)

    return dp[-1][-1]
grid = [
    [5, 3],
    [2, 1]
]
print(most_profitable_path(grid))  # Expected output: 9






grid = [
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
]
print(most_profitable_path(grid))  # Expected output: 16





def unique_paths(grid):
    if not grid or not grid[0]:
        return 0
    dp=[[-1] *len(grid[i]) for i in range(len(grid)) ]
    for i in range(0,len(grid)):
        for j in range(0, len(grid[i])):
            if i ==0 or j ==0:
                dp[i][j] =1
            else:
                dp[i][j]= dp[i][j-1] + dp[i-1][j]

    return dp[-1][-1]
grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(unique_paths(grid))



grid = [[0], [0], [0], [0], [0]]
print(unique_paths(grid))

grid = []
print(unique_paths(grid))
