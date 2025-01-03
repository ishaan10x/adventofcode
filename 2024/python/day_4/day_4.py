with open("day_4/input.txt") as file:
    data = file.read()

grid = [list(line) for line in data.splitlines()]
xmas_occurence = 0

HEIGHT = len(grid)
WIDTH = len(grid[1])

translations = (
    (1, 0),   # Move right
    (-1, 0),  # Move left
    (0, 1),   # Move down
    (0, -1),  # Move up
    (1, 1),   # Move diagonally bottom-right
    (-1, -1), # Move diagonally top-left
    (1, -1),  # Move diagonally bottom-left
    (-1, 1)   # Move diagonally top-right
)

expected_letters = (
    "M", # Second letter
    "A", # Third letter
    "S" # Fourth letter
)

for row in range(HEIGHT):
    for col in range(WIDTH):
        if grid[row][col] == "X":
            print(f"Found X at: {(row,col)}:")
            # For each occurence of X, check for XMAS in all directions
            for dx, dy in translations:
                try:
                    position = (row,col)
                    print(f"    Applying translation ({dx}, {dy}):")
        
                    for i in range(3):
                        position = (position[0] + dx, position[1] + dy)
                        print(f"        New positon: {position}")

                        # Check to ensure position is within bounds
                        if position[0] < 0 or position[0] > HEIGHT - 1:
                            raise ValueError(f"        Y value {position[0]} is out of range, skipping this translation.")
                        if position[1] < 0 or position[1] > WIDTH - 1:
                            raise ValueError(f"        X value {position[1]} is out of range, skipping this translation.")

                        # Check for correct letter
                        if grid[position[0]][position[1]] == expected_letters[i]:
                            print(f"        Correct Letter {grid[position[0]][position[1]]} matches {expected_letters[i]}, keep going!")
                            pass
                        else:
                            raise ValueError(f"        Bad letter encountered {grid[position[0]][position[1]]} expected {expected_letters[i]}, skipping this translation.")
                    
                    xmas_occurence += 1
                    print(f"        CORRECT SEQUENCE, total occurence is {xmas_occurence}")
                except ValueError as e:
                    #print(str(e))
                    pass

print("\nResult: ", xmas_occurence)