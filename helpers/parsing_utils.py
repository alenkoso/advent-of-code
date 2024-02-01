# parsing_utils.py

def read_input_file(file_path):
    ### Read a file and return the content as a list of lines. ###
    with open(file_path, 'r') as file:
        return file.readlines()
    
def read_input_file_strip_lines(file_path):
    ### Read a file and return the content as a list of lines stripped of whitespaces. ###
    with open(file_path, 'r') as file:
        return file.read().strip().split("\n")

def split_lines_to_integers(lines):
    ### Split each line by whitespace and convert to integers. ###
    return [list(map(int, line.split())) for line in lines]

def parse_csv_line(line, cast_type=int):
    ### Parse a CSV line to a list of values with a specified type. ###
    return [cast_type(x) for x in line.split(',')]

def read_input_file_to_grid(file_path):
    ###
    #Reads an input file and converts it into a 2D list (grid).
    # 
    # Parameters:
    # - file_path (str): The path to the input file.
    # 
    # Returns:
    # - grid (List[List[str]]): A 2D list representing the grid of values from the input file.
    
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid
