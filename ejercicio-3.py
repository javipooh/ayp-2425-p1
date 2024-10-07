def is_path_crossing(path: str) -> bool:
    current_position = (0, 0)
    visited_positions = set()
    visited_positions.add(current_position)
    
    moves = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    
    for step in path:
        move_x, move_y = moves[step]
        current_position = (current_position[0] + move_x, current_position[1] + move_y)
        
        if current_position in visited_positions:
            return True
        
        visited_positions.add(current_position)
    
    return False

def main():
    assert is_path_crossing("NES") == False
    print('1-pass')
    assert is_path_crossing("NESWW") == True
    print('2-pass')
    print('ok')

if __name__ == "__main__":
    main()
