import numpy as np
import pandas as pd
import time

def main():

    rope_bridge_df = pd.read_table('adventofcode.com_2022_day_9_input.txt', delimiter=' ', names=['direction', 'steps'])
    rope_bridge_df['steps'] = rope_bridge_df.steps.astype(int)

    walk_field = pd.DataFrame(0, index=range(4000), columns=range(4000)).values
    tail_history = pd.DataFrame(0, index=range(4000), columns=range(4000)).values

    HEAD = 2
    TAIL = 1

    walk_field[2000,2000] = HEAD + TAIL

    start = time.time()

    print('Starting...\n')
    for index, row in rope_bridge_df.iterrows():
        make_move(row[0], row[1], walk_field=walk_field, tail_history=tail_history)


        if (index + 1) % 100 == 0:
            end = time.time()
            print(f"Row {index + 1}. Time Elapsed: {end - start}")

    part_one = tail_history.sum()
    print(f"the tail goes into {part_one} positions at least one time") 



def find_location(walk_field:np.ndarray):

    if len(tuple(np.argwhere(walk_field == 3))) == 0:
        
        head_location = tuple(
            np.argwhere(walk_field == 2)[0]
        )

        tail_location = tuple(
            np.argwhere(walk_field == 1)[0]
        )

        return [head_location, tail_location]
    else:
        
        position = tuple(
            np.argwhere(walk_field == 3)[0]
        )
        
        return [position, position]
    



def calculate_distance(walk_field:np.ndarray):
    
    location = find_location(walk_field)
    
    
    position_head = np.array(location[0])
    position_tail = np.array(location[1])
 
    dist = np.linalg.norm(position_head - position_tail)
    
    return dist
 


def make_move(directions:str, steps:int, walk_field:np.array, tail_history:np.array, HEAD=2, TAIL=1):
    
    for number in range(steps):
        
        position_head, position_tail = find_location(walk_field)
        
        walk_field[position_head] -= HEAD
        
        
        tail_history[position_tail] = 1
        
        match directions:
            case 'R':
                new_position = (position_head[0], (position_head[1] + 1))
                walk_field[new_position] += HEAD
                
                distance = calculate_distance(walk_field)
                
                column_position = position_head[1] - position_tail[1]
                row_position = position_head[0] - position_tail[0]
                
                if distance > 2:
                    walk_field[position_tail] -= TAIL
                    
                    if row_position == 0: 
                        walk_field[position_tail[0], (position_tail[1] + 1)] += TAIL
                    else:
                        walk_field[position_tail[0] + row_position, (position_tail[1] + 1)] += TAIL
            
            case 'L':
                new_position = (position_head[0], (position_head[1] - 1))
                walk_field[new_position] += HEAD
                
                distance = calculate_distance(walk_field)
                
                column_position = position_head[1] - position_tail[1]
                row_position = position_head[0] - position_tail[0]
                
                if distance > 2:
                    walk_field[position_tail] -= TAIL
                    
                    if row_position == 0:
                        walk_field[position_tail[0], (position_tail[1] - 1)] += TAIL
                    else:
                        walk_field[position_tail[0] + row_position, (position_tail[1] - 1)] += TAIL
            
            case 'U':
                new_position = ((position_head[0] - 1), position_head[1])
                walk_field[new_position] += HEAD
                
                distance = calculate_distance(walk_field)
                
                column_position = position_head[1] - position_tail[1]
                row_position = position_head[0] - position_tail[0]
                
                if distance > 2:
                    walk_field[position_tail] -= TAIL
                    
                    if column_position == 0:
                        walk_field[(position_tail[0] - 1), position_tail[1]] += TAIL
                    else:
                        walk_field[(position_tail[0] - 1), (position_tail[1] + column_position)] += TAIL

            
            case 'D':
                new_position = ((position_head[0] + 1), position_head[1])
                walk_field[new_position] += HEAD
                
                distance = calculate_distance(walk_field)
                
                column_position = position_head[1] - position_tail[1]
                row_position = position_head[0] - position_tail[0]
                
                if distance > 2:
                    walk_field[position_tail] -= TAIL
                    
                    if column_position == 0:
                        walk_field[(position_tail[0] + 1), position_tail[1]] += TAIL
                    else:
                        walk_field[(position_tail[0] + 1), (position_tail[1] + column_position)] += TAIL
            








if __name__ == "__main__":
    import numpy
    import pandas
    import time
    main()
