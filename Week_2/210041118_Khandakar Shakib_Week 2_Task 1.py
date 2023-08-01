def process_instructions(instructions:str, grid_size:tuple):
    fp = [0, 0, 90]
    directions = {
        90: (0, 1, "N"),
        0: (1, 0, "E"),
        270: (0, -1, "S"),
        180: (-1, 0, "W")
    }

    for i in instructions:
        if i == 'F':
            fp[0] += directions[fp[2]][0]
            fp[1] += directions[fp[2]][1]
            # Check if the rovers position is out of bound
            if (fp[0] < 0): fp[0] = 0
            if (fp[0] >= grid_size[0]): fp[0] = grid_size[0] - 1
            
            if (fp[1] < 0): fp[1] = 0
            if (fp[1] >= grid_size[1]): fp[1] = grid_size[1] - 1

        elif i == 'L':
            fp[2] = (fp[2] + 90)%360
        elif i == 'R':
            fp[2] = (fp[2] - 90)%360
    
    return (fp[0], fp[1], directions[fp[2]][2])


instructions = "FFLFFRFL"
grid_size = (5, 5)
print(process_instructions(instructions, grid_size))
