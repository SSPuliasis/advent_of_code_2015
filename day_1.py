def calculate_floor(inputfile):
    inputfile = open(inputfile, 'r')
    puzzle_input =inputfile.read()
    start_floor = 0
    floors_up = puzzle_input.count('(')
    floors_down = puzzle_input.count(')')
    floor = start_floor + floors_up - floors_down
    print(floor)
    inputfile.close()
    
# part 2
def get_basement_position(inputfile):
    inputfile = open(inputfile, 'r')
    puzzle_input =inputfile.read()
    start_position = 0
    floor = 0
    for character in puzzle_input:
        start_position +=1
        if character == '(':
            floor += 1
            if floor != -1:
                continue
            else:
                print(start_position)
                break
        elif character == ')':
            floor -= 1
            if floor != -1:
                continue
            else:
                print(start_position)
                break
