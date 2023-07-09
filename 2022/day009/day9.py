# Define the directions and the offsets for each direction
directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

# Read the input file and split it by newlines
with open("adventofcode.com_2022_day_9.txt", "r") as f:
    data = f.read().split("\n")

# Initialize the head and tail positions as (0, 0)
head = (0, 0)
tail = (0, 0)

# Initialize a set to store the visited positions by the tail
visited = set()
# Loop through each motion in the input
for motion in data:
    # Parse the direction and the steps from the motion
    if len(motion.split()):
        direction, steps = motion.split()
        steps = int(steps)

        # Loop for each step in the motion
        for i in range(steps):
            # Update the head position by adding the offset for the direction
            head = tuple(map(sum, zip(head, directions[direction])))
            
            # Add the tail position to the visited set
            visited.add(tail)
            
            # Check if the head and tail are touching or in the same row or column
            if abs(head[0] - tail[0]) + abs(head[1] - tail[1]) <= 1:
                # Do nothing
                pass
            else:
                
                a = ( -(-(tail[0] + head[0] - tail[0]) // abs(head[0] - tail[0])) if abs(head[0] - tail[0]) != 0 else (tail[0] + head[0] - tail[0]))
                b = ( -(-(tail[1] + head[1] - tail[1]) // abs(head[1] - tail[1])) if abs(head[1] - tail[1]) !=0 else (tail[1] + head[1] - tail[1])) 
                #a = ((tail[0] + head[0] - tail[0]) // abs(head[0] - tail[0]))
                #b = ((tail[1] + head[1] - tail[1]) // abs(head[1] - tail[1]))
                # Update the tail position by moving it one step diagonally towards the head
                tail = (a,b)


            # Add the tail position to the visited set
            visited.add(tail)

# Print the size of the visited set as the answer
print(visited)
print(f"The tail of the rope visits {len(visited)} positions at least once.")
