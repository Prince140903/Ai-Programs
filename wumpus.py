import random 

grid = [['' for _ in range(4)] for _ in range(4)] 
wumpus_location = (random.randint(0, 3), random.randint(0, 3)) 
grid[wumpus_location[0]][wumpus_location[1]] = 'W' 
gold_location = (random.randint(0, 3), random.randint(0, 3)) 
grid[gold_location[0]][gold_location[1]] = 'G' 
num_pits = 3 
pit_locations = [] 
for _ in range(num_pits): 
    pit_location = (random.randint(0, 3), random.randint(0, 3)) 
    while pit_location == wumpus_location or pit_location == gold_location or pit_location in pit_locations: 
        pit_location = (random.randint(0, 3), random.randint(0, 3)) 
    pit_locations.append(pit_location) 
    grid[pit_location[0]][pit_location[1]] = 'P' 
user_position = (0, 0) 
while True: 
    grid[user_position[0]][user_position[1]] = 'A' 
    print("Current Grid:") 
    for row in grid: 
        print(row) 
 
    move = input("Enter your move (up, down, left, right): ") 
    grid[user_position[0]][user_position[1]] = '' 
    if move == 'up' and user_position[0] > 0: 
        user_position = (user_position[0] - 1, user_position[1]) 
    elif move == 'down' and user_position[0] < 3: 
        user_position = (user_position[0] + 1, user_position[1]) 
    elif move == 'left' and user_position[1] > 0: 
        user_position = (user_position[0], user_position[1] - 1) 
    elif move == 'right' and user_position[1] < 3: 
        user_position = (user_position[0], user_position[1] + 1) 
    else: 
        print("Invalid move. Try again.") 
        continue 
 
    if user_position == gold_location: 
        print("Congratulations! You found the gold!") 
        break 
    if user_position == wumpus_location: 
        print("Game Over! You encountered the Wumpus.") 
        break 
    if user_position in pit_locations: 
        print("Game Over! You fell into a pit.") 
        break 